from Tools import *
from math import *


class BaseEntity(pygame.sprite.Sprite):  # Базовое существо
    RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3  # Константы направления
    ANGLE = 90  # Угол поворота

    EntityImage = load_image("NoneTexture.png")  # Стандартная текстура

    def __init__(self, x, y, group, direction=UP):
        super().__init__(group)
        self.ImageList = [pygame.transform.rotate(self.EntityImage, 90 * i) for i in range(4)]
        self.direction = direction  # Установка направления
        self.group = group

        self.hp = 100  # Очки прочности
        self.speed = 0  # Максимальная скорость
        self.is_moving = False  # Движение танка

        self.image = self.ImageList[self.direction]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, solid_blocks, entities):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
        if self.is_moving:
            x, y = self.rect.topleft
            dx = cos(radians(BaseEntity.ANGLE * self.direction)) * self.speed  # Расчет проекции на Ox
            dy = - (sin(radians(BaseEntity.ANGLE * self.direction)) * self.speed)  # Расчет проекции на Oy
            self.rect = self.rect.move(dx, dy)
            if pygame.sprite.spritecollide(self, solid_blocks, False) or \
                    len(pygame.sprite.spritecollide(self, entities, False)) != 1:
                self.rect = self.rect.move(-dx, -dy)

        if not pygame.Rect.colliderect(self.rect, screen_rect):
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


class Player(BaseEntity):  # Базовый игрок
    EntityImage = load_image("NoneTexture.png")

    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 3
        self.forbidden = []
        self.center = self.rect.x + self.rect.width, self.rect.y + self.rect.height

    def update(self, solid_blocks, entities):
        for block in pygame.sprite.spritecollide(self, solid_blocks, dokill=False):
            if self.center[0] < block.center[0]:
                pass
        super().update(solid_blocks, entities)

    def shoot(self, direction):  # Стрельба
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

        Bullet(self, x, y)

    def get_event(self, event):
        pass


class FirstPlayer(Player):
    EntityImage = load_image("FirstPlayerTank.png")

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

    def get_event(self, event):  # Обработка событий
        key = pygame.key.get_pressed()
        # Стрельба
        if key[pygame.K_SPACE]:
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

    def __init__(self, owner, x, y):
        super().__init__(x, y, owner.group, direction=owner.direction)
        self.owner = owner
        self.speed = 8
        self.is_moving = True

    def update(self, solid_blocks, entities):
        super().update(solid_blocks, entities)
