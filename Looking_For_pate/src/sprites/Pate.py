import pygame
import os

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)

class Pate(pygame.sprite.Sprite):
    def __init__(self):

        super(Pate, self).__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "Pate.PNG")
        )

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 200