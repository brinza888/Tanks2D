import pygame
from Location import Level
import Blocks

pygame.init()
size = width, height = 608, 608
screen = pygame.display.set_mode(size)


class Canvas(Level):
    map = [[0] * (width // 32) for i in range(height // 32)]

    def on_click(self, mouse_pos):
        x, y = mouse_pos[0] // 32, mouse_pos[1] // 32
        if x is None or y is None:
            return
        self.map[y][x] = (self.map[y][x] + 1) % len(Blocks.get_blocks())
        self.reload()


running = True
canvas = Canvas()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(*canvas.map, sep=",\n")

        if event.type == pygame.MOUSEBUTTONDOWN:
            canvas.on_click(event.pos)
        elif event.type == pygame.MOUSEMOTION and 1 in event.buttons:
            canvas.on_click(event.pos)

    canvas.render(screen)
    pygame.display.flip()

pygame.quit()
