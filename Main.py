import pygame
from Location import location

pygame.init()
size = width, height = (1216, 1216)
screen = pygame.display.set_mode(size)
running = True

loc = location(screen)
loc.render()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
