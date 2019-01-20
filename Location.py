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

        self.wall = pygame.sprite.Sprite()
        self.wall.image = ""
        self.wall.rect = self.wall.image.get_rect()

        self.path = pygame.sprite.Sprite()
        self.path.image = ""
        self.path.rect = self.path.image.get_rect()
        self.reload_board()

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
                    pygame.draw.rect(self.screen, (255, 255, 255), coords, 1)

                if self.board[y][x] == 2:
                    self.path.topleft = y, x

                if self.board[y][x] == 3:
                    self.wall.topleft = y, x
