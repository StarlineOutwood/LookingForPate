import pygame
import os

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)


class Door(pygame.sprite.Sprite):
    """Class of the Doors that lead to other rooms

    Attributes:
        next_room: what room does this door lead to. The value is an integer
        x, y: the coordinates
        px, py: the placement on the map-matrix
    """
    def __init__(self, next_room, x=0, y=0, px=0, py=0, size=100):
        """Creates a door

        Args:
            next room: where does this door lead to
            x, y: x and y coordinates whe drawn
            px, py: placement x and y coordinates in the map-matrix
         """
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "Wall_V.PNG"))
        self.image = pygame.transform.scale(self.image, (size, size))
        self.px = px
        self.py = py

        self.rect = self.image.get_rect()
        self.rect.x = x # pylint: disable=invalid-name
        self.rect.y = y # pylint: disable=invalid-name
        self.next_room = next_room

