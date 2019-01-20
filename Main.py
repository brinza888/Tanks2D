import pygame
import Location
import Entities


pygame.init()
size = width, height = 608, 608
screen = pygame.display.set_mode(size)
running = True

level = Location.FirstLevel()

while running:
    for event in pygame.event.get():
        level.on_event(event)
        if event.type == pygame.QUIT:
            running = False

    level.draw(screen)
    level.update()
    pygame.display.flip()

pygame.quit()
