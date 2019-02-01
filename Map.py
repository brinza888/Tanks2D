from Tools import *
from Blocks import get_block_by_id


class Map:
    def __init__(self, board=[], group=""):
        self.board = board
        self.group = group
        self.cell_size = 32
        self.rows = 608 // 32
        self.cells = 608 // 32

    def generate_map(self):
        for row in range(self.rows):
            for cell in range(self.cells):
                block = get_block_by_id(self.board[row][cell])(row * self.cell_size, cell * self.cell_size, self.group)
                self.group.add(block)
        print(self.group)

