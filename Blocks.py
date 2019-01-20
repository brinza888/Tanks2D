import pygame
import Texture


class __Block (pygame.sprite.Sprite):
    Image = None

    def __init__(self, group, x, y, h=0):
        super().__init__(group)
        self.image = self.__class__.Image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.h = h  # Высота подъема блока над землей (0 - можно ходить, 1 - нельзя)

    # Изменение положения блока
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    # Вызывается, когда существо стоит на нём
    def standing(self, entity):
        pass


class Grass (__Block):
    Image = Texture.load_image("grass.png")


class Stone (__Block):
    Image = Texture.load_image("stone.png")


class Sand (__Block):
    Image = Texture.load_image("sand.png")


__blocks = []
for cls in __Block.__subclasses__():
    __blocks.append(cls)


def get_blocks():
    return __blocks.copy()

# 0 - Grass, 1 - Stone, 2 - Sand

def get_by_id(id):
    try:
        return __blocks[id]
    except IndexError as er:
        print("get_by_id error:", er)
