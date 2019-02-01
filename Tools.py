import os
import pygame
from Logging import Logger


pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

logger = Logger()


def load_image(name, color_key=None):
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        if color_key is not None:
            if color_key is -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        return image
    except pygame.error as ex:
        logger.write(ex, logger.ERROR)
