from Tools import *


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            logger.write("Game force quited", type=logger.ACTION)
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
