from Tools import *
from GameUI import *
from Map import Map
from MapList import get_map_wrapper
from Entities import FirstPlayer, SecondPlayer


def game(game_map, _screen):
    game_running = True

    while game_running:
        for event in pygame.event.get():

            game_map.get_event()

            if event.type == pygame.QUIT:
                terminate()

        _screen.fill((0, 0, 0))

        game_map.update()
        game_map.draw(_screen)

        pygame.display.flip()


def menu(_screen):
    main_menu = MainMenu()

    menu_running = True
    while menu_running:
        for event in pygame.event.get():

            ret = main_menu.get_event(event)
            if ret is not None:
                return ret

            if event == pygame.QUIT:
                terminate()

        _screen.fill((0, 0, 0))

        main_menu.draw(_screen)

        pygame.display.flip()


running = True
while running:
    map_id = menu(screen)
    game_map = Map(get_map_wrapper(map_id), FirstPlayer, SecondPlayer)
    game(game_map, screen)
