from Tools import *
from math import *


class BaseEntity(pygame.sprite.Sprite):  # Базовое существо
    RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3  # Константы направления
    ANGLE = 90  # Угол поворота

    EntityImage = load_image("NoneTexture.png")  # Стандартная текстура
    Colliding = True
    DefaultHp = 10
    Invulnerability = False

    def __init__(self, x, y, group, direction=UP):
        super().__init__(group)
        self.ImageList = [pygame.transform.rotate(self.EntityImage, 90 * i) for i in range(4)]
        self.direction = direction  # Установка направления
        self.group = group

        self.hp = self.DefaultHp  # Очки прочности
        self.speed = 0  # Максимальная скорость
        self.is_moving = False  # Движение танка
        self.killed = False

        self.image = self.ImageList[self.direction]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, solid_blocks, entities):
        if self.is_moving:
            dx = cos(radians(BaseEntity.ANGLE * self.direction)) * self.speed  # Расчет проекции на Ox
            dy = - (sin(radians(BaseEntity.ANGLE * self.direction)) * self.speed)  # Расчет проекции на Oy
            self.rect = self.rect.move(dx, dy)
            if self.Colliding:
                if pygame.sprite.spritecollideany(self, solid_blocks) or \
                        len(pygame.sprite.spritecollide(self, entities, False)) != 1:
                    self.rect = self.rect.move(-dx, -dy)

        if not pygame.Rect.colliderect(self.rect, screen_rect):
            self.kill()

        if self.hp <= 0:
            self.kill()

    def get_event(self, event):
        pass

    def set_direction(self, direction):  # Смена направления
        self.image = self.ImageList[direction]
        x, y = self.rect.x, self.rect.y
        self.direction = direction
        self.image = pygame.transform.rotate(self.EntityImage, BaseEntity.ANGLE * self.direction)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def get_damage(self, damage):
        if not self.Invulnerability:
            self.hp -= damage

    def kill(self):
        super(BaseEntity, self).kill()
        self.killed = True


class Player(BaseEntity):  # Базовый игрок
    EntityImage = load_image("NoneTexture.png")
    Shoot_sound = load_sound("shoot.wav")

    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 3
        self.counter = 0
        self.bullet = None

    def update(self, solid_blocks, entities):
        super().update(solid_blocks, entities)
        if self.bullet and self.bullet.killed:
            self.bullet = None

        if self.hp <= 0:
            self.kill_player()

    def shoot(self, direction):  # Стрельба
        if self.bullet is not None:
            return
        x, y = self.rect.x, self.rect.y
        if direction == 0 or direction == 2:
            y += 15
            if direction == 0:
                x += 32
            else:
                x -= 16
        elif direction == 1 or direction == 3:
            x += 15
            if direction == 1:
                y -= 16
            else:
                y += 32
        Player.Shoot_sound.stop()
        Player.Shoot_sound.play()
        self.bullet = Bullet(self, x, y)

    def kill_player(self):
        self.counter += 1
        kill = pygame.event.Event(pygame.USEREVENT, score=self.counter, killed=self.Name)
        pygame.event.post(kill)

    def get_event(self, event):
        pass


class FirstPlayer(Player):
    EntityImage = load_image("FirstPlayerTank.png")
    Name = "First"

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
    Name = "Second"

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
    EntityImage = load_image("Bullet.png")
    Colliding = False

    def __init__(self, owner, x, y):
        super().__init__(x, y, owner.group, direction=owner.direction)
        self.owner = owner
        self.speed = 8
        self.damage = 10
        self.is_moving = True

    def update(self, solid_blocks, entities):
        super(Bullet, self).update(solid_blocks, entities)
        block = pygame.sprite.spritecollideany(self, solid_blocks)
        if block is not None:
            block.get_damage(self.damage)
            self.kill()
            return
        entity = pygame.sprite.spritecollideany(self, entities)
        if entity not in (None, self, self.owner):
            entity.get_damage(self.damage)
            self.kill()

