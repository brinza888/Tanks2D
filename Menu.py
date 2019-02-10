from Tools import *


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, group):
        super(Button, self).__init__(group)
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color("Gray"), (0, 0, self.w, self.h))
        self.rect = pygame.Rect((self.x, self.y, self.w, self.h))

    def update(self, event):
        return self.rect.collidepoint(*event.pos)


class LevelButton(Button):
    def __init__(self, x, y, w, h, group, map_id):
        super(LevelButton, self).__init__(x, y, w, h, group)
        self.map_id = map_id

    def update(self, event):
        if self.rect.collidepoint(*event.pos):
            return self.map_id


def menu():
    buttons = pygame.sprite.Group()
    start_game = Button(100, 50, 400, 100, buttons)
    fon = pygame.transform.scale(load_image('menu.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    button_text = "Start Game"
    start_game.image.blit(*text(button_text, 150, 40, pygame.Color("Black")))

    green_text = ["Зеленый игрок: ", "W - Вперед", "A - Влево",
                  "S - Вниз", "D - Вправо", "Пробел - Выстрел"]

    red_text = ["Красный игрок:", "^ - Вперед", "< - Влево",
                "v - Вниз", "> - Вправо", "Enter - Выстрел"]

    y = 200
    for num in range(len(red_text)):
        screen.blit(*text(green_text[num], 400, y, pygame.Color("Green")))
        screen.blit(*text(red_text[num], 50, y, pygame.Color("Red")))
        y += 60

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game.update(event):
                    return change_level()
        buttons.draw(screen)
        pygame.display.flip()


def change_level():
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
                    menu()
        screen.fill((0, 0, 0))
        levels.draw(screen)
        counter = 0
        for level in levels:
            counter += 1
            level.image.blit(*text(str(counter) + " LVL", 22, 10, pygame.Color("Black")))
        pygame.display.flip()
