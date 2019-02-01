from Tools import *
import Map
from Blocks import load_blocks

running = True
logger.write("Game started", logger.ACTION)


blocks = pygame.sprite.Group()

load_blocks()


map = Map()
# Матрица с картой
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            logger.write("Game quited", logger.ACTION)
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
logger.write("Game exited", logger.ACTION)
