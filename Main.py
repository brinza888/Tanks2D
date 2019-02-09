from Tools import *
from Map import Map
from Blocks import load_blocks
from MapList import get_map_wrapper
from Menu import menu
from Entities import FirstPlayer, SecondPlayer


def game():
    load_blocks()

    board = get_map_wrapper(0).Map

    try:
        level = Map(board, FirstPlayer, SecondPlayer)
        level.generate_map()
    except Exception as ex:
        logger.write("Level generation fatal error: {}".format(ex), logger.ERROR)
        logger.write("Game interrupted because fatal error".format(ex), logger.INFO)
        exit(0)

    level.spawn_players()

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

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu()
                        game()

            screen.fill((0, 0, 0))
            level.draw(screen)
            level.update()

            pygame.display.flip()
            clock.tick(50)
        except Exception as ex:
            logger.write("Exception in game: {}".format(ex), logger.ERROR)

    pygame.quit()
    logger.write("Game quited", logger.INFO)


menu()
game()
