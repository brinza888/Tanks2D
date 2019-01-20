import pygame


class Location(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        # Значения по умолчанию
        self.board = []
        self.cell_size = 32
        self.width = 1216 // self.cell_size
        self.height = 1216 // self.cell_size
        self.all_sprites = pygame.sprite.Group()
        self.screen = screen
        self.reload_board()

    def reload_board(self):
        for y in range(self.height):
            temp = []
            for x in range(self.width):
                temp.append(True)
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
                pygame.draw.rect(self.screen, (255, 255, 255), coords, 1)
