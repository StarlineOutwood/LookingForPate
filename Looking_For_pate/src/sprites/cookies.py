import pygame
import os

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)


class Cookie(pygame.sprite.Sprite):
    """Class of Esterosh's gingersnap cookies

    Attributes:
        x, y: its x and y coordinates
        image: the image we use for cookies
    """
    def __init__(self, x=0, y=0, px=0, py=0, size=100):
        """Creates Pate that we need to find

        Args:
            x, y: the x and y coordinates where we want to place our little ratboy
         """

        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "assets", "Gingersnap_Cookies.PNG")
        )
        self.image = pygame.transform.scale(self.image, (size*0.5, size*0.5))
        self.rect = self.image.get_rect()
        self.rect.x = x # pylint: disable=invalid-name
        self.rect.y = y # pylint: disable=invalid-name
        self.px=px
        self.py=py

    def eat(self):
        self.kill()
