import pygame
from sprites.Laudna import Laudna
from sprites.Pate import Pate

class Room:
    def __init__(self, room_map, room_size):
        self.room_size = room_size
        self.Laudna = None
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(room_map)

    def _initialize_sprites(self, room_map):
        height = len(room_map)
        width = len(room_map[0])

        