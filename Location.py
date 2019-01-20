import pygame
import Blocks
import Entities


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

    def __init__(self, x=0, y=0):
        super().__init__()
        # Значения по умолчанию
        self.cell_size = 32
        self.width = len(self.map[0])
        self.height = len(self.map)
        # Тайлы
        self.tiles = pygame.sprite.Group()
        self.cords = self.x, self.y = x, y
        self.reload()
        # Существа в уровне
        self.entities = pygame.sprite.Group()
        self.human = Entities.Human(self.entities, 128, 128)

    def reload(self):
        for i, row in enumerate(self.map):
            for j, block_id in enumerate(row):
                bx = self.x + self.cell_size * j
                by = self.y + self.cell_size * i
                Blocks.get_by_id(block_id)(self.tiles, bx, by)

    def change_cell_size(self, size):
        self.cell_size = size

    def draw(self, screen):
        self.tiles.draw(screen)
        self.entities.draw(screen)

    def update(self):
        pass

    def on_event(self, event):
        for entity in self.entities:
            entity.on_event(event)



class FirstLevel(Level):
    map = [[4, 2, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 3],
           [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0],
           [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 2, 0, 2, 2, 0, 2, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
           [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 1, 0],
           [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 0, 1, 1, 2, 1, 0],
           [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0],
           [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1, 1, 0],
           [0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1, 2, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


class SecondLevel(Level):
    pass
