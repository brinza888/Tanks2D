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

    def __init__(self, screen, x=0, y=0):
        super().__init__()
        # Значения по умолчанию
        self.cell_size = 32
        self.width, self.height = len(Level.map[0]), len(Level.map)
        self.table = [pygame.sprite.Group() for x in range(self.height)]
        self.screen = screen
        self.coords = self.x, self.y = x, y
        self.map = []
        for i, row in enumerate(Level.map):
            temp = []
            for j, block_id in enumerate(row.split()):
                block = Blocks.get_by_id(int(block_id))()
                temp.append(block)
                self.table[i].add(block)
            self.map.append(temp)

    def change_cell_size(self, size):
        self.cell_size = size

    def render(self):
        for row in range(self.height):
            for cell in range(self.width):
                self.map[row][cell].rect.topleft = row * self.cell_size, cell * self.cell_size


class FirstLevel(Level):
    map = ["1 1 1 1 1",
           "1 1 1 1 1",
           "1 1 1 1 1"]
    height, width = len(map), len(map[0])


class SecondLevel(Level):
    map = load_map("")
    height, width = len(map), len(map[0])
