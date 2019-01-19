import pygame

GRAVITY = 10


class Entity (pygame.sprite.Sprite):
    def __init__(self, x, y, group, image):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.health = 100
        self.attack = 0
        self.speed = 0
        self.ground = None

    def update(self, *args):
        if not self.ground:
            self.rect.y -= GRAVITY

    def get_event(self, event):
        pass


class Person (Entity):
    def __init__(self, x, y, group, image):
        super().__init__(x, y, group, image)  # calling super class
        self.speed = 5

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.speed
            elif event.key == pygame.K_LEFT:
                self.rect.x -= self.speed
