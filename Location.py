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


class Levels:
    map = None
    height, width = None, None

    def __init__(self, screen):
        super().__init__()
        # Значения по умолчанию
        self.cell_size = 32
        self.width = width
        self.height = height
        self.screen = screen

        self.grass = Blocks.Grass.image
        self.sand = Blocks.Sand.image
        self.stone = Blocks.stone.image


    def reload_board(self):
        for y in range(self.height):
            temp = []
            for x in range(self.width):
                temp.append(1)
            self.board.append(temp)

    def change_cell_size(self, size):
        self.cell_size = size
        self.width = 1216 // self.cell_size
        self.height = 1216 // self.cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                coords = (x * self.cell_size, y * self.cell_size,
                          self.cell_size, self.cell_size)

                if self.board[y][x] == 1:
                    self.grass.topleft = y, x

                if self.board[y][x] == 2:
                    self.sand.topleft = y, x

                if self.board[y][x] == 3:
                    self.stone.topleft = y, x


class First_lvl(Levels):
    map = load_map("Map.txt")
    height, width = len(map), len(map[0])


class Second_lvl(Levels):
    map = load_map("")
    height, width = len(map), len(map[0])