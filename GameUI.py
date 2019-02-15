from Tools import *


class BaseForm (pygame.sprite.Group):
    def __init__(self, x, y, w, h, bg_color=pygame.Color("Gray")):
        super(BaseForm, self).__init__()
        self.w, self.h = w, h
        self.x, self.y = x, y
        self.bg_color = bg_color

    def add(self, *sprites):
        super(BaseForm, self).add(*sprites)
        for element in sprites:
            element.rect.x = self.x + element.x
            element.rect.y = self.y + element.y

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.w, self.h))
        super(BaseForm, self).draw(surface)

    def get_event(self, event):
        for element in self.sprites():
            element.get_event(event)


class BaseElement (pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super(BaseElement, self).__init__()
        self.w, self.h = w, h
        self.x, self.y = x, y
        self.color = color

        self.image = pygame.Surface((self.w, self.h))
        pygame.draw.rect(self.image, self.color, (0, 0, self.w, self.h))
        self.rect = self.image.get_rect()

    def get_event(self, event):
        pass


class MessageBox (BaseForm):
    def __init__(self, message, *args, **kwargs):
        super(MessageBox, self).__init__(*args, **kwargs)
        self.message = message

    def draw(self, surface):
        super(MessageBox, self).draw(surface)
        surface.blit(self.message, (self.x, self.y))
        for button in self.sprites():
            surface.blit(button.image, (button.rect.x, button.rect.y))


class Button (BaseElement):
    def __init__(self, button_text, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.image.blit(button_text, (0, 0))
        self.rect.x = self.x
        self.rect.y = self.y

    def on_click(self):
        print("Ну нажал ты на меня, и что?")  # действие по клику на кнопку
        return id(self)


class MapButton (Button):
    pattern = "{}LVL"

    def __init__(self, map_id, *args, **kwargs):
        self.map_id = map_id
        super(MapButton, self).__init__(*args, **kwargs)

    def on_click(self):
        return self.map_id


class Menu (BaseForm):
    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)
        self.selected = None

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in self.sprites():
                if element.rect.collidepoint(event.pos) and isinstance(element, Button):
                    return element.on_click()


class MainMenu (Menu):
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        self.add(Button(text("Начать игру", pygame.Color("Red")), 200, 100, 200, 100, pygame.Color("Gray")))
        self.add(Button(text("Инструкции", pygame.Color("Red")), 200, 300, 200, 100, pygame.Color("Gray")))


class LevelMenu(Menu):
    def __init__(self, *args, **kwargs):
        super(LevelMenu, self).__init__(*args, **kwargs)
        size = (89, 89)
        counter = 0
        for y in range(50, 468, 139):
            for x in range(50, 468, 139):
                counter += 1
                self.add(MapButton(counter, text("Map " + str(counter),
                            pygame.Color("Red")), x, y, *size, pygame.Color("Gray")))


if __name__ == "__main__":  # для тестирования классов интерфейса

    # menu = MainMenu(*screen_rect, pygame.Color("Black"))

    # menu = LevelMenu(*screen_rect, pygame.Color("Black"))

    # menu = MessageBox(text("MessageBox 1", pygame.Color("Red")), 100, 100, 400, 400)
    # menu.add(Button(text("Дизайн", pygame.Color("Red")), 200, 100, 100, 100, pygame.Color("Black")))

    running = True
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        menu.draw(screen)
        pygame.display.flip()

    pygame.quit()
