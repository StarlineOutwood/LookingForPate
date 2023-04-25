import pygame
import os

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)


class Door(pygame.sprite.Sprite):
    def __init__(self, next_room, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "Wall_V.PNG"))
        self.image = pygame.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()
        self.rect.x = x # pylint: disable=invalid-name
        self.rect.y = y # pylint: disable=invalid-name
        self.next_room = next_room

    def next(self):
        return self.next_room
