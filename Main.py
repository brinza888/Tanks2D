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


menu = Menu(*screen_rect)
running = True

while running:
    for event in pygame.event.get():
        id = menu.get_event(event)
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))



    menu.draw(screen)

    pygame.display.flip()
