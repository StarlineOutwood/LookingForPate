import pygame
import os
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)

class Laudna(pygame.sprite.Sprite):
    def __init__(self):

        super(Laudna, self).__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "Laudna.PNG")
        )

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def move(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)