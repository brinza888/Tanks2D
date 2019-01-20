import pygame
import Texture


class __Entity(pygame.sprite.Sprite):
    Image = None

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = self.__class__.Image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.health = 100
        self.damage = 10

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def on_event(self, event):
        pass


class Human(__Entity):
    Image = Texture.load_image("sand.png")

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.move(0, -32)
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.move(0, 32)
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                self.move(32, 0)
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.move(-32, 0)


__entities = []
for cls in __Entity.__subclasses__():
    __entities.append(cls)


def get_blocks():
    return __entities.copy()


def get_by_id(id):
    try:
        return __entities[id]
    except IndexError as er:
        print("get_by_id error:", er)
