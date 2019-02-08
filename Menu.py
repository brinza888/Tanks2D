from Tools import *


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, group, w=400, h=100):
        super(Button, self).__init__(group)
        self.x, self.y = x, y
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color("Gray"), (0, 0, w, h))
        self.rect = pygame.Rect((self.x, self.y, w, h))

    def update(self, event):
        return self.rect.collidepoint(*event.pos)


def menu():
    buttons = pygame.sprite.Group()
    start_game = Button(100, 100, buttons)
    make_level = Button(100, 400, buttons)

    fon = pygame.transform.scale(load_image('NoneTexture.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text = ["Start Game", "Make level"]

    string_rendered = font.render(text[0], 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 40
    intro_rect.x = 150
    start_game.image.blit(string_rendered, intro_rect)

    string_rendered = font.render(text[1], 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 40
    intro_rect.x = 150
    make_level.image.blit(string_rendered, intro_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game.update(event):
                    return
                if make_level.update(event):
                    pass
        buttons.draw(screen)
        pygame.display.flip()