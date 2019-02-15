from Tools import *
from GameUI import *
from Map import Map
from MapList import get_map_wrapper
from Entities import FirstPlayer, SecondPlayer
from Blocks import load_blocks


def game(game_map, _screen):
    game_running = True
    message_box = None

    game_map.generate_map()

    game_map.spawn_player1()
    game_map.spawn_player2()

    game_map.scores_to_zero()

    clock = pygame.time.Clock()

    while game_running:
        for event in pygame.event.get():
            if not game_map.end[0]:
                ended = game_map.get_event(event)
                if ended:
                    if game_map.end[1] is FirstPlayer:
                        winner_name = "First Player win"
                        color = pygame.Color("Green")
                    else:
                        winner_name = "Second Player win"
                        color = pygame.Color("Red")

                    x, y = width // 2 - 96, height // 2 - 96
                    message_box = MessageBox(text(winner_name, color), x, y, 200, 100)
                    message_box.add(Button("Back to Menu", text("Вернуться в меню", pygame.Color("Black")),
                             0, 50, 200, 100, color))

            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_running = False

            if ended:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in message_box:
                        if button.rect.collidepoint(event.pos):
                            return

        _screen.fill((0, 0, 0))

        game_map.draw(_screen)

        if not game_map.end[0]:
            game_map.update()
        elif message_box is not None:
            message_box.draw(_screen)

        pygame.display.flip()
        clock.tick(50)


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

            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu = MainMenu(*rect)
                continue

        _screen.fill((0, 0, 0))

        menu.draw(_screen)

        pygame.display.flip()


pygame.mixer.music.load('music/MainTheme.wav')
pygame.mixer.music.set_volume(0.75)
pygame.mixer.music.play(-1)

load_blocks()

running = True
while running:
    map_id = menu(screen, screen_rect)
    game_map = Map(get_map_wrapper(map_id), FirstPlayer, SecondPlayer)
    game(game_map, screen)
