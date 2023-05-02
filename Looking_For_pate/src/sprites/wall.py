import pygame
import os

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)


class Wall(pygame.sprite.Sprite):
    """Class for walls or "borders" of the game

    Attributes:
        x, y: coordinates
        image: image we use for the wall
    """
    def __init__(self, x=0, y=0, horizontal=True, size=100):
        """Creates a wall

        Args:
            x, y: the x and y coordinates of the wall
            horizontal: wather or not it is a horizontal wall or not
         """
        super().__init__()

        if horizontal:
            self.image = pygame.image.load(
                os.path.join(dirname, "assets", "Wall_H.PNG")
            )
            self.image = pygame.transform.scale(self.image, (size, size))
        else:
            self.image = pygame.image.load(
                os.path.join(dirname, "assets", "Wall_H.PNG")
            )
            self.image = pygame.transform.scale(self.image, (size*0.5, size))
        self.rect = self.image.get_rect()
        self.rect.x = x # pylint: disable=invalid-name
        self.rect.y = y # pylint: disable=invalid-name
