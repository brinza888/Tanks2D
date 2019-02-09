from Tools import *
from Map import Map
from Blocks import load_blocks
from MapList import get_map_wrapper
from Menu import menu
from Entities import FirstPlayer, SecondPlayer


def game(map_id):
    load_blocks()
    board = get_map_wrapper(map_id).Map
    try:
        level = Map(board, FirstPlayer, SecondPlayer)
        level.generate_map()
    except Exception as ex:
        logger.write("Level generation fatal error: {}".format(ex), logger.ERROR)
        logger.write("Game interrupted because fatal error".format(ex), logger.INFO)
        exit(0)
    level.spawn_players()
    clock = pygame.time.Clock()
    logger.write("Game started", logger.INFO)
    running = True

    while running:
        try:
            for event in pygame.event.get():
                level.get_event(event)
                if event.type == pygame.QUIT:
                    terminate()
                    logger.write("User closed game window", logger.ACTION)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            screen.fill((0, 0, 0))
            level.draw(screen)
            level.update()
            pygame.display.flip()
            clock.tick(50)
        except Exception as ex:
            logger.write("Exception in game: {}".format(ex), logger.ERROR)


while True:
    game(menu())
