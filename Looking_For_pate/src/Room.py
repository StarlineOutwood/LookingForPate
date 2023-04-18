import pygame
from sprites.Laudna import Laudna
from sprites.Pate import Pate
from sprites.wall import Wall
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

class Room:
    def __init__(self, room_size, room_map):
        self.room_size = room_size
        self.Laudna = None
        self.Pate = None
        self.walls_V = pygame.sprite.Group()
        self.walls_H = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(room_map)

    def _initialize_sprites(self, room_map):
        height = len(room_map)
        width = len(room_map[0])  

        for y in range(height):
            for x in range(width):
                spot = room_map[y][x]
                real_y = y * self.room_size
                real_x = x * self.room_size
                if spot == 1:
                    self.Laudna = Laudna(real_x, real_y)
                elif spot == 2:
                    self.Pate = Pate(real_x, real_y) 
                elif spot == 3:
                    self.walls_H.add(Wall(real_x, real_y, True))
                elif spot == 4:
                    self.walls_V.add(Wall(real_x, real_y, False))

        self.all_sprites.add(self.walls_H, self.walls_V, self.Pate)

