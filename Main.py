from Tools import *
from Map import Map
from Blocks import load_blocks
from MapList import get_map_wrapper
from Menu import menu
from Entities import FirstPlayer, SecondPlayer


def game(map_id):
    map = get_map_wrapper(map_id)
    try:
        level = Map(map, FirstPlayer, SecondPlayer)
        level.generate_map()
    except Exception as ex:
        logger.write("Level generation fatal error: {}".format(ex), logger.ERROR)
        exit(0)

    level.spawn_player1()
    level.spawn_player2()

    clock = pygame.time.Clock()
    logger.write("Game started", logger.INFO)
    running = True

    while running:
        try:
            for event in pygame.event.get():
                if not level.end[0]:
                    level.get_event(event)

                if event.type == pygame.QUIT:
                    terminate()
                    logger.write("User closed game window", logger.ACTION)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            screen.fill((0, 0, 0))
            level.draw(screen)

            if not level.end[0]:
                level.update()
            else:
                pass  # вот тут if level.end[0]

            pygame.display.flip()
            clock.tick(50)
        except Exception as ex:
            logger.write("Exception in game: {}".format(ex), logger.ERROR)


logger.write("Game loaded", logger.INFO)


try:
    pygame.mixer.music.load("music/Maintheme.wav")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)
except pygame.error as ex:
    logger.write("Can load theme music: {}".format(ex), logger.ERROR)


try:
    load_blocks()
except Exception as ex:
    logger.write("Load blocks fatal error: {}".format(ex), logger.ERROR)
    exit(0)


while True:
    try:
        game(menu())
    except Exception as ex:
        logger.write("Fatal error in Game or Menu: {}".format(ex), logger.ERROR)
