from Tools import *


class BaseForm (pygame.sprite.Group):
    def __init__(self, x, y, w, h, bg_color=pygame.Color("Gray")):
        super(BaseForm, self).__init__()
        self.w, self.h = w, h
        self.x, self.y = x, y
        self.bg_color = bg_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.w, self.h))

    def add(self, *sprites):
        super(BaseForm, self).add(*sprites)
        for element in sprites:
            element.rect.x = self.x + element.x
            element.rect.y = self.y + element.y

    def get_event(self, event):
        for element in self.sprites():
            element.get_event(event)


class BaseElement (pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, group):
        super(BaseElement, self).__init__(group)
        self.w, self.h = w, h
        self.x, self.y = x, y

        self.image = pygame.Surface((self.w, self.h))
        self.rect = self.image.get_rect()

    def get_event(self, event):
        pass


class MessageBox (BaseForm):
    def __init__(self, message, *args, **kwargs):
        super(MessageBox, self).__init__(*args, **kwargs)
        self.message = message
        self.text = "Кнопка"
        self.buttons = []

    def append(self, button):
        self.buttons.append(button)

    def draw(self, surface):
        super(MessageBox, self).draw(surface)
        surface.blit(self.message, (self.x, self.y))
        for button in self.buttons:
            surface.blit(button.image, (self.x + button.rect.x, self.y  + button.rect.y))


class Button (BaseElement):
    def __init__(self, button_text, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)
        self.image.blit(button_text, (self.w // 2, self.h // 2))
        self.rect.x = self.x
        self.rect.y = self.y

    def on_click(self, event):
        print(self.rect.collidepoint(event.pos))
        print(event.pos, self.rect)
        if self.rect.collidepoint(event.pos):
            print("Ну нажал ты на меня, и что?")


class MapButton (Button):
    pattern = "{}LVL"

    def __init__(self, map_id, *args, **kwargs):
        self.map_id = map_id
        button_text = MapButton.pattern.format(map_id)
        super(MapButton, self).__init__(button_text=button_text, *args, **kwargs)

    def on_click(self):
        return self.map_id


class Menu (BaseForm):
    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)
        self.selected = None

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in self.sprites():
                if element.rect.collidepoint(*event) and isinstance(element, Button):
                    return element.on_click()


if __name__ == "__main__":  # для тестирования классов интерфейса
    mb = MessageBox(text("MessageBox 1", pygame.Color("Red")), 100, 100, 200, 200)
    mb.append(Button(text("Button1", pygame.Color("Red")), 0, 50, 200, 50, mb))
    print(mb.buttons)
    running = True
    while running:
        for ev in pygame.event.get():
            mb.update(ev)
            if ev.type == pygame.QUIT:
                running = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for button in mb.buttons:
                    button.on_click(ev)

        screen.fill((100, 100, 100))
        mb.draw(screen)
        pygame.display.flip()

    pygame.quit()
