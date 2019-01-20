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

    def __init__(self, screen, x=0, y=0):
        super().__init__()
        # Значения по умолчанию
        self.cell_size = 32
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.group = pygame.sprite.Group()
        self.coords = self.x, self.y = x, y
        self.reload()

    def reload(self):
        for i, row in enumerate(self.map):
            for j, block_id in enumerate(row.split()):
                bx = self.x + self.cell_size * j
                by = self.y + self.cell_size * i
                Blocks.get_by_id(block_id)(self.group, bx, by)
        self.human_coords = [128, 128]
        self.human = Entities.Human(self.group, *self.human_coords)

    def change_cell_size(self, size):
        self.cell_size = size

    def render(self, screen):
        self.group.draw(screen)

    def get_event(self, event, dx=0, dy=0):
        if event == "Human":
            if 0 <= self.human_coords[0] + dx < 608 \
                    and 0 <= self.human_coords[1] + dy < 608:
                self.human_coords[0] += dx
                self.human_coords[1] += dy
                self.human.move(*self.human_coords)


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
