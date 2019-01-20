import pygame
import Location


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
running = True


level = Location.FirstLevel(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    level.render(screen)
    pygame.display.flip()

pygame.quit()
