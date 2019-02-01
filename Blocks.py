from Tools import *


class BaseBlock(pygame.sprite.Sprite):
    BlockImage = load_image("NoneTexture.png")

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = self.BlockImage
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        pass


class Bricks(BaseBlock):
    BlockImage = load_image("Bricks64.png")
