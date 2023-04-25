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
    def __init__(self, x=0, y=0):

        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "Laudna.PNG")
        )

        self.rect = self.image.get_rect()
        self.rect.x = x # pylint: disable=invalid-name
        self.rect.y = y # pylint: disable=invalid-name

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, pressed_keys, walls_H, walls_V):
        if pressed_keys[K_UP]:
            if self.can_move(walls_H, 0, -5):
                # enough to check if it hits any roof aka a horizontal wall
                if self.can_move(walls_V, 0, -5):
                    self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            if self.can_move(walls_H, 0, 5):
                self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            if self.can_move(walls_V, -5, 0):
                self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            if self.can_move(walls_V, 5, 0):
                self.rect.move_ip(5, 0)

    def colliding_Pate(self, pate):
        if pygame.sprite.collide_rect(self, pate):
            return False  # Do we continue the game? if pate is found we dont
        return True

    def colliding_Door(self, door):
        if pygame.sprite.collide_rect(self, door):
            return True
        return False

    def can_move(self, walls, x=0, y=0):
        self.rect.move_ip(x, y)
        colliding_walls = pygame.sprite.spritecollide(self, walls, False)
        can_move = not colliding_walls
        self.rect.move_ip(-x, -y)
        return can_move
