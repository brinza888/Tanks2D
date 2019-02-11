from Tools import *
from GameUI import *


def menu():
    buttons = pygame.sprite.Group()
    start_game = Button(100, 50, 400, 100, buttons)
    instruction_button = Button(100, 300, 400, 100, buttons)
    fon = pygame.transform.scale(load_image('menu.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    button_text = ["Начать игру", "Инструкции"]
    start_game.image.blit(*text(button_text[0], 150, 40, pygame.Color("Black")))
    instruction_button.image.blit(*text(button_text[1], 150, 40, pygame.Color("Black")))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game.update(event):
                    return change_level()
                elif instruction_button.update(event):
                    return instruction()
        buttons.draw(screen)
        pygame.display.flip()


def instruction():
    fon = pygame.transform.scale(load_image('menu.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    button = pygame.sprite.Group()
    green_text = ["Зеленый игрок: ", "W - Вперед", "A - Влево",
                  "S - Вниз", "D - Вправо", "Пробел - Выстрел"]

    red_text = ["Красный игрок:", "^ - Вперед", "< - Влево",
                "v - Вниз", "> - Вправо", "Enter - Выстрел"]

    escape = "Escape - Выход в главное меню"
    text_on_button = "Назад"
    back_to_menu = Button(100, 20, 400, 60, button)
    back_to_menu.image.blit(*text(text_on_button, 165, 20, pygame.Color("Black")))
    y = 200
    for num in range(len(red_text)):
        screen.blit(*text(green_text[num], 400, y, pygame.Color("Green")))
        screen.blit(*text(red_text[num], 50, y, pygame.Color("Red")))
        y += 60
    screen.blit(*text(escape, 150, 120, pygame.Color("White")))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return menu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_menu.update(event):
                    return menu()
        button.draw(screen)
        pygame.display.flip()


def change_level():
    fon = pygame.transform.scale(load_image('menu.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    size = (89, 89)
    levels = pygame.sprite.Group()
    counter = 1
    for y in range(50, 468, 139):
        for x in range(50, 468, 139):
            LevelButton(x, y, *size, levels, map_id=counter)
            counter += 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for level in levels:
                    map_id = level.update(event)
                    if map_id:
                        return map_id

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return menu()

        levels.draw(screen)
        counter = 0
        for level in levels:
            counter += 1
            level.image.blit(*text(str(counter) + " Map", 18, 10, pygame.Color("Black")))
        pygame.display.flip()
