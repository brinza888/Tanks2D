from Tools import *


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, group, color=pygame.Color("Gray")):
        super(Button, self).__init__(group)
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.image = pygame.Surface((w, h), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, color, (0, 0, self.w, self.h))
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


class MessageBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, group, color=pygame.Color("Gray")):
        super(MessageBox, self).__init__(group)
        self.x, self.y, self.w, self.h = x, y, w, h
        self.color = color
        self.image = pygame.Surface((self.w, self.h), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, color, (0, 0, self.w, self.h))
        self.rect = pygame.Rect((self.x, self.y, self.w, self.h))
        self.restart = Button(x, y + h // 2, w, (h + 1) // 2, group, pygame.Color("Green"))
        self.restart.image.blit(*text("Вернуться в меню?", x, h // 4 - 5, pygame.Color("Black")))

    def update(self, event):
        return self.restart.update(event)
