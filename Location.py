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
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.group = pygame.sprite.Group()
        self.screen = screen
        self.cords = self.x, self.y = x, y
        for i, row in enumerate(self.map):
            for j, block_id in enumerate(row.split()):
                bx = self.x + self.cell_size * j
                by = self.y + self.cell_size * i
                Blocks.get_by_id(int(block_id))(self.group, bx, by)

    def change_cell_size(self, size):
        self.cell_size = size

    def render(self, screen):
        self.group.draw(screen)


class FirstLevel(Level):
    map = ["1 1 1 1 1",
           "1 2 1 1 1",
           "1 1 1 1 1"]


class SecondLevel(Level):
    pass
