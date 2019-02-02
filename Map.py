from Tools import *
from Blocks import *
from Entities import Player


class Map:
    def __init__(self, board):
        self.board = board
        self.up_blocks = pygame.sprite.Group()  # Группа верхних блоков (для отрисовки)
        self.down_blocks = pygame.sprite.Group()  # Группа нижних блоков (для отрисовки)
        self.entities = pygame.sprite.Group()  # Группа существ
        self.solid_blocks = pygame.sprite.Group()  # Группа твердых блоков (для столкновений)

        self.cell_size = 32
        self.rows = height // self.cell_size
        self.cells = width // self.cell_size

    def generate_map(self):
        for row in range(self.rows):
            for cell in range(self.cells):
                block = get_block_by_id(self.board[row][cell])
                if block.Layer == BaseBlock.UP:
                    b = block(row * self.cell_size, cell * self.cell_size, self.up_blocks)
                else:
                    b = block(row * self.cell_size, cell * self.cell_size, self.down_blocks)
                if b.Solid:
                    self.solid_blocks.add(b)

                if block is PlayerSpawn:
                    Player(row * self.cell_size, cell * self.cell_size, self.entities)

    def draw(self, _screen):
        self.down_blocks.draw(_screen)
        self.entities.draw(_screen)
        self.up_blocks.draw(_screen)

    def update(self):
        self.down_blocks.update()
        self.entities.update(self.solid_blocks, self.entities)
        self.up_blocks.update()

    def get_event(self, event):
        for bl in self.down_blocks:
            bl.get_event(event)
        for ent in self.entities:
            ent.get_event(event)
        for bl in self.up_blocks:
            bl.get_event(event)
