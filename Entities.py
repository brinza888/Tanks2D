from Tools import *
from math import *
from Blocks import PlayerFlag


class BaseEntity(pygame.sprite.Sprite):  # Базовое существо
    RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3  # Константы направления
    ANGLE = 90  # Угол поворота

    EntityImage = load_image("NoneTexture.png")  # Стандартная текстура
    Colliding = True   # может ли существо сталкиваться
    DefaultHp = 10  # очки жизни при создании существа
    Invulnerability = False  # присуща ли неубиваемость

    def __init__(self, x, y, group, direction=UP):
        super().__init__(group)
        # лист изображений с разным направлением существа
        self.ImageList = [pygame.transform.rotate(self.EntityImage, 90 * i) for i in range(4)]
        self.direction = direction  # Установка направления
        self.group = group

        self.hp = self.DefaultHp  # Очки прочности
        self.speed = 0  # Максимальная скорость
        self.is_moving = False  # Движение танка
        self.killed = False  # убито ли существо

        self.image = self.ImageList[self.direction]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, solid_blocks, entities):
        if self.is_moving:
            dx = cos(radians(BaseEntity.ANGLE * self.direction)) * self.speed  # Расчет проекции на Ox
            dy = - (sin(radians(BaseEntity.ANGLE * self.direction)) * self.speed)  # Расчет проекции на Oy
            self.rect = self.rect.move(dx, dy)
            if self.Colliding:  # обработка столкновений
                if pygame.sprite.spritecollideany(self, solid_blocks) or \
                        len(pygame.sprite.spritecollide(self, entities, False)) != 1:
                    self.rect = self.rect.move(-dx, -dy)  # откидываем противника назад

        if not pygame.Rect.colliderect(self.rect, screen_rect):
            self.kill()  # если существо за экраном, убиваем его

    def get_event(self, event):  # метод для обработки событий
        pass

    def set_direction(self, direction):  # Смена направления
        self.image = self.ImageList[direction]
        x, y = self.rect.x, self.rect.y
        self.direction = direction
        self.image = pygame.transform.rotate(self.EntityImage, BaseEntity.ANGLE * self.direction)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def get_damage(self, damage):  # получение урона
        if not self.Invulnerability:
            self.hp -= damage
        if self.hp <= 0:
            self.kill()
            return True

    def kill(self):  # переопределям метод на смерть существа
        super(BaseEntity, self).kill()
        self.killed = True


class Player(BaseEntity):  # Базовый игрок
    EntityImage = load_image("NoneTexture.png")
    Shoot_sound = load_sound("shoot.wav")

    Name = "NonePlayer"
    Scores = 0
    BulletImage = load_image("NoneTexture.png")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = 2
        self.counter = 0
        self.bullet = None
        self.Invulnerability = True

    def update(self, solid_blocks, entities):
        super().update(solid_blocks, entities)
        if self.Invulnerability and (self.is_moving or self.bullet):
            self.Invulnerability = False
        if self.bullet and self.bullet.killed:  # если пуля столкнулась, то разрешить стрельбу
            self.bullet = None

    def shoot(self, direction):  # Стрельба
        if self.bullet is not None:  # нельзя стрелять, пока прошлая пуля существует
            return
        x, y = self.rect.x, self.rect.y
        # вычисляем координаты, откуда полетит пуля
        if direction == 0 or direction == 2:
            y += self.rect.height // 2
            if direction == 0:
                x += self.rect.width
            else:
                x -= self.rect.width // 2
        elif direction == 1 or direction == 3:
            x += self.rect.width // 2
            if direction == 1:
                y -= self.rect.height // 2
            else:
                y += self.rect.height
        Player.Shoot_sound.stop()  # звуки стрельбы
        Player.Shoot_sound.play()
        self.bullet = Bullet(self, x, y)  # создаем пулю


class FirstPlayer(Player):
    EntityImage = load_image("FirstPlayerTank.png")
    BulletImage = load_image("FirstBullet.png")

    def get_event(self, event):  # Обработка событий
        key = pygame.key.get_pressed()
        # Стрельба
        if key[pygame.K_SPACE]:
            self.shoot(self.direction)
        # Движение танка
        self.is_moving = True
        if key[pygame.K_w]:
            self.set_direction(self.UP)
        elif key[pygame.K_s]:
            self.set_direction(self.DOWN)
        elif key[pygame.K_d]:
            self.set_direction(self.RIGHT)
        elif key[pygame.K_a]:
            self.set_direction(self.LEFT)
        else:
            self.is_moving = False


class SecondPlayer(Player):  # Противник
    EntityImage = load_image("SecondPlayerTank.png")
    BulletImage = load_image("SecondBullet.png")

    def get_event(self, event):  # Обработка событий
        key = pygame.key.get_pressed()
        # Стрельба
        if key[pygame.K_RETURN]:
            self.shoot(self.direction)
        # Движение танка
        self.is_moving = True
        if key[pygame.K_UP]:
            self.set_direction(self.UP)
        elif key[pygame.K_DOWN]:
            self.set_direction(self.DOWN)
        elif key[pygame.K_RIGHT]:
            self.set_direction(self.RIGHT)
        elif key[pygame.K_LEFT]:
            self.set_direction(self.LEFT)
        else:
            self.is_moving = False


class Bullet(BaseEntity):  # Снаряд
    EntityImage = load_image("NoneTexture.png")
    Colliding = False

    def __init__(self, owner, x, y):
        self.EntityImage = owner.BulletImage  # установка картинки пули, которая присуща игроку-владельцу
        super().__init__(x, y, owner.group, direction=owner.direction)
        self.owner = owner
        self.speed = 8
        self.damage = 10
        self.is_moving = True

    def update(self, solid_blocks, entities):
        super(Bullet, self).update(solid_blocks, entities)

        block = pygame.sprite.spritecollideany(self, solid_blocks)
        if block is not None:  # проверка столкновений с блоками
            if not (isinstance(block, PlayerFlag) and isinstance(self.owner, block.pclass)):
                killed = block.get_damage(self.damage)
                if killed and isinstance(block, PlayerFlag):
                    ev = pygame.event.Event(pygame.USEREVENT, scores=200, player=self.owner)
                    pygame.event.post(ev)  # отправляем событие, что игрок-владелец уничтожил флаг противника
            self.kill()

        entity = pygame.sprite.spritecollideany(self, entities)
        if entity not in (None, self, self.owner):  # проверка столкновений с существами
            killed = entity.get_damage(self.damage)

            if killed and entity.__class__ is not Bullet:  # Проверка убито ли существо
                ev = pygame.event.Event(pygame.USEREVENT, scores=10, player=self.owner)
                pygame.event.post(ev)  # отправляем событие, что игрок-владелец убил существо
            self.kill()

