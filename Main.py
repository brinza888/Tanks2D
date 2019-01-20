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
        if event.type == pygame.QUIT:
            running = False
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                level.get_event("Human", dy=-32)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                level.get_event("Human", dy=32)
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                level.get_event("Human", dx=-32)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                level.get_event("Human", dx=32)

    level.render(screen)
    pygame.display.flip()

pygame.quit()
