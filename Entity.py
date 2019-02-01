from Tools import *
from math import sin, cos, radians


class BaseEntity(pygame.sprite.Sprite):
    EntityImage = load_image("NoneTexture.png")

    RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3

    def __init__(self, x, y, group, direction=UP):
        super().__init__(group)
        self.direction = direction
        self.image = pygame.transform.rotate(self.EntityImage, 90 * self.direction)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pygame.mask.from_surface(self.image)
        self.hp = 100
        self.speed = 0
        self.is_moving = False
        self.damage_protection = 0

    def update(self):
        if self.is_moving:
            dx = cos(radians(90 * self.direction)) * self.speed
            dy = - (sin(radians(90 * self.direction)) * self.speed)
            self.rect = self.rect.move(dx, dy)

    def get_event(self, event):
        pass

    def set_direction(self, facing):
        x, y = self.rect.x, self.rect.y
        self.direction = facing
        self.image = pygame.transform.rotate(self.EntityImage, 90 * self.direction)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class Player(BaseEntity):
    EntityImage = load_image("PlayerTank.png")

    def __init__(self, *args):
        super().__init__(*args)
        self.speed = 3

    def shoot(self):
        Bullet(self, self.rect.x, self.rect.y)

    def get_event(self, event):
        self.is_moving = True
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.shoot()
        elif key[pygame.K_w]:
            self.set_direction(self.UP)
        elif key[pygame.K_s]:
            self.set_direction(self.DOWN)
        elif key[pygame.K_d]:
            self.set_direction(self.RIGHT)
        elif key[pygame.K_a]:
            self.set_direction(self.LEFT)
        else:
            self.is_moving = False


class Enemy(BaseEntity):
    EntityImage = load_image("EnemyTank.png")


class Bullet(BaseEntity):
    EntityImage = load_image("Bullet.png")

    def __init__(self, owner, *args):
        super().__init__(*args, direction=owner.direction)
        self.owner = owner
        self.speed = 25
        self.is_moving = True


class Fortifying(BaseEntity):
    EntityImage = load_image("Fortifying.png")

    def __init__(self, team, *args):
        super().__init__(*args)
        self.team = team

    def update(self):
        if self.hp <= 0:
            self.team.lose()
            self.kill()
