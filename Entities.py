import pygame

GRAVITY = 10


# Base class for all game entities
class Entity (pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()  # calling Sprite class constructor
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.health = None
        self.attack = None
        self.speed = None

    def update(self, *args):
        pass

    # method for handling events
    def get_event(self, event):
        pass


# Person (player) entity
class Person (Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.speed = 1

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.speed
            elif event.key == pygame.K_LEFT:
                self.rect.x -= self.speed
