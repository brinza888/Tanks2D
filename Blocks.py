from Tools import *


# Базовый класс для всех блоков
class BaseBlock(pygame.sprite.Sprite):
    UP, DOWN = 0, 1  # Константы слоев

    BlockImage = load_image("NoneTexture.png")  # Стандартная текстура
    Layer = UP  # Слой отрисовки
    Solid = True  # Твердость
    DefaultHp = 10  # Начальные очки прочности
    Indestructible = False

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = self.BlockImage
        self.hp = self.DefaultHp
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def get_damage(self, damage):
        if not self.Indestructible:
            self.hp -= damage
        if self.hp <= 0:
            self.kill()
            return True

    def get_event(self, event):
        pass

    def update(self, entities):
        pass


class Air(BaseBlock):
    BlockImage = load_image("Air.png")
    Layer = BaseBlock.DOWN
    Solid = False


class Barrier(BaseBlock):
    BlockImage = load_image("Barrier.png")
    Indestructible = True


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
    DefaultHp = 20
    second_image = load_image("DamagedBricks.png")

    def get_damage(self, damage):
        super(Bricks, self).get_damage(damage)
        self.image = self.second_image


class Iron(BaseBlock):
    BlockImage = load_image("Iron.png")
    Indestructible = True


class Bushes (BaseBlock):
    BlockImage = load_image("Bushes.png")
    Solid = False
    Layer = BaseBlock.UP


class PlayerFlag:
    DefaultHp = 50

    def __init__(self, *args):
        super(PlayerFlag, self).__init__(*args)
        self.pclass = None


class FirstPlayerFlag (PlayerFlag, BaseBlock):
    BlockImage = load_image("FirstPlayerFlag.png")


class SecondPlayerFlag (PlayerFlag, BaseBlock):
    BlockImage = load_image("SecondPlayerFlag.png")


# Поиск и загрузка существующих блоков (от класса BaseBlock)
__blocks = []


def load_blocks():
    id_list = ""
    for i, cls in enumerate(BaseBlock.__subclasses__()):
        __blocks.append(cls)
        id_list += "Block '{}' with ID {}\n".format(cls.__name__, i)
    logger.write("ID list:\n{}".format(id_list), logger.INFO)


# Возвращает класс блока по данному ID
def get_block_by_id(id):
    try:
        return __blocks[id]
    except IndexError:
        logger.write("Block with ID {} doesn't exist".format(id), logger.ERROR)
        return BaseBlock
