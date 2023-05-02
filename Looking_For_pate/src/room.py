import pygame
from sprites.laudna import Laudna
from sprites.pate import Pate
from sprites.wall import Wall
from sprites.door import Door
from sprites.cookies import Cookie


class Room:
    """Class of the room or the game layout

    Attributes:
        room_size: the size of the room
        room_map: the map or layout of the room
        Laudna: laudna of this room
        Pate: Pate of this room, if pate excists in this room
        walls_V, walls_H: vertical and horizontal walls of the room
        Doors: what doors the roomhas
        all_sprites: all of the sprites in this room, except Laudna
    """
    def __init__(self, room_size, room_map, doors):
        """Creates The room that we moved to

        Args:
            room_size: what is the size of the room
            room_map: what is the layout of the room
            doors: where the doors lead from this room
         """
        self.room_size = room_size
        self.map = room_map
        self.Laudna = None
        self.Pate = None
        self.walls_V = pygame.sprite.Group()
        self.walls_H = pygame.sprite.Group()
        self.Doors = pygame.sprite.Group()
        self.cookies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(room_map, doors, room_size)

    def _initialize_sprites(self, room_map, doors, room_size):
        """Creates all the sprites in the wanted room

        Args:
            room_map: what is the layout of the room
            doors: where the doors lead from this room
         """
        height = len(room_map)
        width = len(room_map[0])
        i = 0
        for y in range(height):
            for x in range(width):
                spot = room_map[y][x]
                real_y = y * self.room_size
                real_x = x * self.room_size
                if spot == 1:
                    self.Laudna = Laudna(real_x, real_y, room_size)
                elif spot == 2:
                    self.Pate = Pate(real_x, real_y, room_size)
                    self.all_sprites.add(self.Pate)
                elif spot == 3:
                    self.walls_H.add(Wall(real_x, real_y, True, room_size))
                elif spot == 4:
                    self.walls_V.add(Wall(real_x, real_y, False, room_size))
                elif spot == 5:
                    self.Doors.add(Door(doors[i], real_x, real_y, x, y, room_size))
                    i += 1
                elif spot == 6:
                    self.cookies.add(Cookie(real_x, real_y, x, y, room_size))

        self.all_sprites.add(self.walls_V, self.walls_H, self.Doors, self.cookies)
