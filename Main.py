from Tools import *
from Map import Map
from Blocks import load_blocks
from MapList import get_map_wrapper
from Menu import menu
from Entities import FirstPlayer, SecondPlayer


def game(map_id):
    fp_points = 0
    sp_points = 0
    board = get_map_wrapper(map_id).Map
    try:
        level = Map(board, FirstPlayer, SecondPlayer)
        level.generate_map()
    except Exception as ex:
        logger.write("Level generation fatal error: {}".format(ex), logger.ERROR)
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
                elif event.type == pygame.USEREVENT:
                    print(event.score)
                    if event.killed == "Second":
                        fp_points = event.score
                    elif event.killed == "First":
                        sp_points = event.score

            screen.fill((0, 0, 0))
            level.draw(screen)
            level.update()
            screen.blit(*text(str(fp_points), 208, 32, pygame.Color("Green")))
            screen.blit(*text(str(sp_points), 408, 32, pygame.Color("Red")))
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
