import pygame

GRAVITY = 10


# Base class for all game entities
class Entity (pygame.sprite.Sprite):
    def __init__(self, x, y, group, image):
        super().__init__(group)  # calling Sprite class constructor
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.health = 100
        self.attack = 0
        self.speed = 0
        self.ground = None  # is standing on rigid block

    def update(self, *args):
        # apply gravity on entity if entity not on rigid block
        if not self.ground:
            self.rect.y -= GRAVITY

    # method for handling events
    def get_event(self, event):
        pass


# Person (player) entity
class Person (Entity):
    def __init__(self, x, y, group, image):
        super().__init__(x, y, group, image)
        self.speed = 5

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.speed
            elif event.key == pygame.K_LEFT:
                self.rect.x -= self.speed
