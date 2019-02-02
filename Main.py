from Tools import *

try:
    from Map import Map
    from Blocks import load_blocks
    from MapList import *
except Exception as ex:
    logger.write("Fatal error in import: {}".format(ex), logger.ERROR)
    logger.write("Game interrupted because fatal error".format(ex), logger.INFO)
    exit(0)


load_blocks()

board = map1

try:
    level = Map(board)
    level.generate_map()
except Exception as ex:
    logger.write("Level generation fatal error: {}".format(ex), logger.ERROR)
    logger.write("Game interrupted because fatal error".format(ex), logger.INFO)
    exit(0)

clock = pygame.time.Clock()

running = True
logger.write("Game started", logger.INFO)

while running:
    try:
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
    except Exception as ex:
        logger.write("Exception in game: {}".format(ex), logger.ERROR)

pygame.quit()
logger.write("Game quited", logger.INFO)
