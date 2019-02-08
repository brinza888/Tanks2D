from Tools import *
from math import sin, cos, radians


class BaseEntity(pygame.sprite.Sprite):
    RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3  # Константы направления
    ANGLE = 90  # Угол поворота

    EntityImage = load_image("NoneTexture.png")

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
            dx = cos(radians(BaseEntity.ANGLE * self.direction)) * self.speed  # Расчет проекции на Ox
            dy = - (sin(radians(BaseEntity.ANGLE * self.direction)) * self.speed)  # Расчет проекции на Oy
            self.rect = self.rect.move(dx, dy)
        if not pygame.Rect.colliderect(self.rect, screen_rect):
            self.kill()

    def get_event(self, event):
        pass

    def set_direction(self, direction):  # Смена направления
        self.image = self.ImageList[direction]
        self.direction = direction


class Player(BaseEntity):  # Игрок
    EntityImage = load_image("FirstPlayerTank.png")

    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 3
        self.forbidden = None

    def update(self, solid_blocks, entities):
        super().update(solid_blocks, entities)

    def shoot(self, direction):  # Стрельба
        x, y = self.rect.x, self.rect.y
        if direction == 0 or direction == 2:
            y += 15
        elif direction == 1 or direction == 3:
            x += 15

        Bullet(self, x, y)

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


class Enemy(BaseEntity):  # Противник
    EntityImage = load_image("EnemyTank.png")


class Bullet(BaseEntity):  # Снаряд
    EntityImage = load_image("Bullet.png")

    def __init__(self, owner, x, y):
        super().__init__(x, y, owner.group, direction=owner.direction)
        self.owner = owner
        self.speed = 8
        self.is_moving = True

    def update(self, solid_blocks, entities):
        super().update(solid_blocks, entities)
