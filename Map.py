from Tools import *
from Blocks import get_block_by_id
from Entities import Player


class Map:
    def __init__(self, board):
        self.board = board
        self.blocks = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()

        self.cell_size = 32
        self.rows = height // self.cell_size
        self.cells = width // self.cell_size

    def generate_map(self):
        for row in range(self.rows):
            for cell in range(self.cells):
                block = get_block_by_id(self.board[row][cell])
                block(row * self.cell_size, cell * self.cell_size, self.blocks)
                if block is get_block_by_id(2):
                    Player(row * self.cell_size, cell * self.cell_size, self.entities)

    def draw(self, _screen):
        self.blocks.draw(_screen)
        self.entities.draw(_screen)

    def update(self):
        self.blocks.update()
        self.entities.update()

    def get_event(self, event):
        for bl in self.blocks:
            bl.get_event(event)
        for ent in self.entities:
            ent.get_event(event)
