import pygame
import os

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, horizontal=True):
        super().__init__()

        if horizontal:
            self.image = pygame.image.load(
                os.path.join(dirname, "assets", "Wall_H.PNG")
            )
            self.image = pygame.transform.scale(self.image, (200, 200))
        else:
            self.image = pygame.image.load(
                os.path.join(dirname, "assets", "Wall_H.PNG")
            )
            self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x # pylint: disable=invalid-name
        self.rect.y = y # pylint: disable=invalid-name
