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
    """Class of Laudna, the character moved by the player

    Attributes:
        image: the picture used for Laudna
        x, y: the x and y coordinates of Laudna
    """
    def __init__(self, x=0, y=0, size=100):
        """Creates Laudna, the Palyer character

        Args:
            x, y = The x and y coordinates where she starts at
         """        

        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "Laudna.PNG")
        )
        self.image = pygame.transform.scale(self.image, (size*0.35, size*0.7))

        self.rect = self.image.get_rect()
        self.rect.x = x # pylint: disable=invalid-name
        self.rect.y = y # pylint: disable=invalid-name

    def draw(self, surface):
        """Draws Laudna

        Args:
            surface: what surface she is being drawn into
         """
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, pressed_keys, walls_H, walls_V):
        """Moves laudna

        Args:
            pressed_keys: which direction we want to go to
            walls_H: horizontal walls
            walls_V: vertical walls
            most likely walls will be changed into just one wall
         """
        if pressed_keys[K_UP]:
            if self.can_move(walls_H, 0, -3):
                if self.can_move(walls_V, 0, -3):
                    self.rect.move_ip(0, -3)
        if pressed_keys[K_DOWN]:
            if self.can_move(walls_H, 0, 3):
                if self.can_move(walls_V, 0, 3):
                    self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            if self.can_move(walls_V, -3, 0):
                if self.can_move(walls_H, -3, 0):
                    self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            if self.can_move(walls_V, 3, 0):
                if self.can_move(walls_H, 3, 0):
                    self.rect.move_ip(3, 0)

    def colliding_Pate(self, pate):
        """Chechs if laudna collides with Pate, aka finds Pate

        Args:
            Pate: pate that we are colliding into
            return: if we should continue the game or not, aka did we find pate or not
         """
        if pygame.sprite.collide_rect(self, pate):
            return False  # Do we continue the game? if pate is found we dont
        return True
    
    def colliding_cookie(self, cookie):
        if pygame.sprite.collide_rect(self, cookie):
            return True
        return False

    def colliding_Door(self, door):
        """Checks if we are colliding into a door

        Args:
            door: door that we are colliding into
            returns: if we collide or not
         """
        if pygame.sprite.collide_rect(self, door):
            return True
        return False

    def can_move(self, walls, x=0, y=0):
        """Checks if we can move or if we are colliding with a wall

        Args:
            walls: walls we are checking for collisions
            x, y: the x and y of which direction and how much we want to move to
         """
        self.rect.move_ip(x, y)
        colliding_walls = pygame.sprite.spritecollide(self, walls, False)
        can_move = not colliding_walls
        self.rect.move_ip(-x, -y)
        return can_move
