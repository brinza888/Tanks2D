from Tools import *
from GameUI import *


def game(game_map, _screen):
    game_running = True

    while game_running:
        for event in pygame.event.get():
            game_map.get_event()
            if event.type == pygame.QUIT:
                game_running = False

        _screen.fill((0, 0, 0))

        game_map.update()
        game_map.draw(_screen)

        pygame.display.flip()


def menu(_screen):
    main_menu = MainMenu()

    menu_running = True
    while menu_running:
        for event in pygame.event.get():

            main_menu.get_event(event)

            if event == pygame.quit():
                menu_running = False

        _screen.fill((0, 0, 0))

        main_menu.draw(_screen)

        pygame.display.flip()


