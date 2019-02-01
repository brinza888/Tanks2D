from Tools import *


# Базовый класс для всех блоков
class BaseBlock(pygame.sprite.Sprite):
    BlockImage = load_image("NoneTexture.png")

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = self.BlockImage
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        pass


class Air(BaseBlock):
    pass


class Border_Block():
    BlockImage = load_image("EnemyTank.png")


class Bricks(BaseBlock):
    BlockImage = load_image("Bricks.png")



__blocks = []


# Поиск существующих блоков
def load_blocks():
    for cls in BaseBlock.__subclasses__():
        __blocks.append(cls)
    print(__blocks)


# Возвращает класс блока по ID
def get_block_by_id(id):
    try:
        return __blocks[id]
    except IndexError:
        logger.write("Block with ID {} doesn't exist".format(id), logger.ERROR)
        return BaseBlock
