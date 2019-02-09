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


def text(text):
    font = pygame.font.Font(None, 30)
    string_rendered = font.render(text, 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 40
    intro_rect.x = 150
    return string_rendered, intro_rect


def menu():
    buttons = pygame.sprite.Group()
    start_game = Button(100, 100, 400, 100, buttons)

    fon = pygame.transform.scale(load_image('NoneTexture.png'), (width, height))
    screen.blit(fon, (0, 0))
    button_text = ["Start Game"]

    start_game.image.blit(*text(button_text[0]))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game.update(event):
                    change_level()
                    return
        buttons.draw(screen)
        pygame.display.flip()


def change_level():
    running = True
    size = (89, 89)
    levels = pygame.sprite.Group()
    for y in range(50, 468, 139):
        for x in range(50, 468, 139):
            Button(y, x, *size, levels)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        screen.fill((0, 0, 0))
        levels.draw(screen)
        pygame.display.flip()
