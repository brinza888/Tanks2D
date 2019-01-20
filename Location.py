import pygame
import Blocks


def load_map(file):
    file = open(file, "rt", encoding="utf8").read().split("\n")
    map = []
    for row in file:
        temp = []
        for cell in row.split():
            temp.append(int(cell))
        map.append(temp)
    return map


class Level:
    map = []

    def __init__(self, x, y, screen):
        super().__init__()
        # Значения по умолчанию
        self.cell_size = 32
        self.width, self.height = len(Level.map[0]), len(Level.map)
        self.table = [pygame.sprite.Group() for x in range(self.height)]
        self.screen = screen
        self.cords = self.x, self.y = x, y
        for i, row in enumerate(Level.map):
            for j, block_id in enumerate(row.split()):
                block = Blocks.get_by_id(int(block_id))()
                block.rect.x, block.rect.y = self.x, self.y
                self.table[i].add(block)

    def change_cell_size(self, size):
        self.cell_size = size
        self.width = 1216 // self.cell_size
        self.height = 1216 // self.cell_size

    def render(self):
        pass


class FirstLevel(Level):
    map = ["1 1 1 1 1",
           "1 1 1 1 1",
           "1 1 1 1 1"]
    height, width = len(map), len(map[0])


class SecondLevel(Level):
    map = load_map("")
    height, width = len(map), len(map[0])
