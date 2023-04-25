import os
import pygame
from sprites.laudna import Laudna
from sprites.pate import Pate
from room import Room
from GameLoop import GameLoop

ROOM_MAP_0 = [[3, 3, 3, 3, 3, 3, 3],
              [4, 0, 0, 0, 0, 0, 5],
              [4, 0, 0, 0, 0, 1, 4],
              [4, 0, 0, 0, 0, 0, 4],
              [3, 3, 3, 3, 3, 3, 3]]

ROOM_MAP_1 = [[3, 3, 3, 3, 3, 3, 3],
              [5, 1, 4, 0, 3, 0, 5],
              [4, 0, 4, 0, 0, 0, 4],
              [4, 0, 0, 0, 3, 0, 4],
              [3, 3, 3, 3, 3, 3, 3]]

ROOM_MAP_2 = [[3, 3, 3, 3, 3, 3, 3],
              [5, 1, 0, 0, 0, 0, 4],
              [4, 0, 0, 0, 0, 0, 4],
              [4, 0, 0, 0, 0, 2, 4],
              [3, 3, 3, 3, 3, 3, 3]]

MAPS = [ROOM_MAP_0, ROOM_MAP_1, ROOM_MAP_2]

DOORS = [[1], [0, 2], [1]]

ROOM_SIZE = 200


def main():
    loop = GameLoop()
    height = len(MAPS[0])
    width = len(MAPS[0][0])
    dis_height = height*ROOM_SIZE
    dis_width = width*ROOM_SIZE
    screen = pygame.display.set_mode((dis_width, dis_height))
    room = Room(ROOM_SIZE, MAPS[0], [1])
    pygame.init()
    room.all_sprites.draw(screen)
    room.Laudna.draw(screen)

    generating = True
    end = False
    while generating:
        next = loop.start(room, screen)
        if next is None:
            generating = False
            end = True
            if loop.end(end):
                next = 0 # pylint: disable=invalid-name
                generating = True
                end = False
        screen = pygame.display.set_mode((dis_width, dis_height))
        room = Room(ROOM_SIZE, MAPS[next], DOORS[next])
        pygame.init()
        room.all_sprites.draw(screen)
        room.Laudna.draw(screen)


if __name__ == "__main__":
    main()
