import pygame
import Location


pygame.init()
size = width, height = 1216, 1216
screen = pygame.display.set_mode(size)
running = True


loc = Location.First_lvl(screen)
loc.render()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()
