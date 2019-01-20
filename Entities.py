import pygame
import Blocks
import Texture


class Entity(pygame.sprite.Sprite):
    Image = None

    def __init__(self, group, x=608//32//2, y=608//32/2):
        self.health = 100
        self.dmg = 10
        super(Entity, self).__init__(group)
        self.image = self.__class__.Image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


class Human(Entity):
    Image = Texture.load_image("sand.png")

    def move(self, x, y):
        self.rect.topleft = x, y

    def coords(self):
        return self.rect.topleft

