from Tools import *
from Map import Map
from Blocks import load_blocks


load_blocks()

board = [[2] + [0] * 18] + [[0] * 7 + [3] * 5 + [0] * 7] + [[0] * 19] * 17

level = Map(board)
level.generate_map()

clock = pygame.time.Clock()

running = True
logger.write("Game started", logger.ACTION)

while running:
    for event in pygame.event.get():
        level.get_event(event)
        if event.type == pygame.QUIT:
            running = False
            logger.write("Game quited", logger.ACTION)

    screen.fill((0, 0, 0))
    level.draw(screen)
    level.update()

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
logger.write("Game exited", logger.ACTION)
