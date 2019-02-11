import os
import sys

import pygame
from Logging import Logger


pygame.init()
size = width, height = 608, 608
screen_rect = pygame.Rect(0, 0, width, height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tanks 2D")

logger = Logger()  # Логирование событий в текстовик


def load_image(name, color_key=None):
    fullname = os.path.join("sprites", name)
    try:
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        if color_key is not None:
            if color_key is -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        return image
    except pygame.error as ex:
        logger.write("Can't load image {} because: {}".format(name, ex), logger.ERROR)


def load_sound(name):
    fullname = os.path.join("music", name)
    try:
        return pygame.mixer.Sound(fullname)
    except pygame.error as ex:
        logger.write("Cant load music {} because: {}".format(name, ex), logger.ERROR)


def text(text, x, y, color):
    font = pygame.font.Font(None, 30)
    string_rendered = font.render(text, 1, color)
    intro_rect = string_rendered.get_rect()
    intro_rect.top = y
    intro_rect.x = x
    return string_rendered, intro_rect


def terminate():
    pygame.quit()
    sys.exit()


def load_background(photo):
    # Photo должно лежать в папке sprites
    return pygame.transform.scale(load_image(photo), (width, height))


pygame.display.set_icon(load_image("icon.png"))
