from Tools import *
from Map import Map
from Blocks import load_blocks
from MapList import *


load_blocks()

board = map1

level = Map(board)
level.generate_map()

clock = pygame.time.Clock()

running = True
logger.write("Game started", logger.INFO)

while running:
    for event in pygame.event.get():
        level.get_event(event)
        if event.type == pygame.QUIT:
            running = False
            logger.write("User closed game window", logger.ACTION)

    screen.fill((0, 0, 0))
    level.draw(screen)
    level.update()

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
logger.write("Game quited", logger.INFO)
