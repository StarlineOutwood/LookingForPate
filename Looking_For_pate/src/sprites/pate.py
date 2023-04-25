import pygame
import os

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)


class Pate(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):

        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "Pate.PNG")
        )
        self.rect = self.image.get_rect()
        self.rect.x = x # pylint: disable=invalid-name
        self.rect.y = y # pylint: disable=invalid-name