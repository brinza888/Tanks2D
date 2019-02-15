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


def menu(_screen, rect):
    menu = MainMenu(*rect)

    menu_running = True
    while menu_running:
        for event in pygame.event.get():

            answer = menu.get_event(event)
            if answer == "start_game":
                menu = LevelMenu(*rect)
                continue
            elif answer == "instructions":
                menu = InstructionsMenu(*rect)
                continue
            elif isinstance(answer, int):
                return answer

            if event == pygame.QUIT:
                terminate()

        _screen.fill((0, 0, 0))

        menu.draw(_screen)

        pygame.display.flip()


running = True
while running:
    map_id = menu(screen, screen_rect)
    game_map = Map(get_map_wrapper(map_id), FirstPlayer, SecondPlayer)
    game(game_map, screen)
