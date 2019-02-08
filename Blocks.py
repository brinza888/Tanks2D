from Tools import *


# Базовый класс для всех блоков
class BaseBlock(pygame.sprite.Sprite):
    UP, DOWN = 0, 1  # Константы слоев

    BlockImage = load_image("NoneTexture.png")  # Стандартная текстура
    Layer = UP  # Слой отрисовки
    Solid = True  # Твердость
    DefaultHp = 10  # Начальные очки прочности

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = self.BlockImage
        self.hp = self.DefaultHp
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.center = self.rect.x + self.rect.width, self.rect.y + self.rect.height

    def update(self):
        if self.hp <= 0:
            self.kill()

    def get_event(self, event):
        pass


class Air(BaseBlock):
    BlockImage = load_image("Air.png")
    Layer = BaseBlock.DOWN
    Solid = False


class Barrier(BaseBlock):
    BlockImage = load_image("Barrier.png")


class FirstPlayerSpawn(BaseBlock):  # Точка возрождения 1 игрока
    BlockImage = load_image("Air.png")
    Layer = BaseBlock.DOWN
    Solid = False


class SecondPlayerSpawn(BaseBlock):  # Точка возрождения 2 игрока
    BlockImage = load_image("Air.png")
    Layer = BaseBlock.DOWN
    Solid = False


class Bricks(BaseBlock):
    BlockImage = load_image("Bricks.png")


class Stone(BaseBlock):
    BlockImage = load_image("Stone.png")


__blocks = []


# Поиск и загрузка существующих блоков (от класса BaseBlock)
def load_blocks():
    for cls in BaseBlock.__subclasses__():
        __blocks.append(cls)


# Возвращает класс блока по данному ID
def get_block_by_id(id):
    try:
        return __blocks[id]
    except IndexError:
        logger.write("Block with ID {} doesn't exist".format(id), logger.ERROR)
        return BaseBlock
