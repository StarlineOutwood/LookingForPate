import os
import pygame
from sprites.laudna import Laudna
from sprites.pate import Pate
from room import Room
from GameLoop import GameLoop
from sprites.door import Door

ROOM_MAP_START = []
ROOM_MAP_0 = []
ROOM_MAP_1 = []
ROOM_MAP_2 = []
ROOM_MAP_3 = []
ROOM_MAP_4 = []
MAPS = []
DOORS = []
ROOM_SIZE = 0

def main():
    loop = GameLoop(ROOM_MAP_START, MAPS, DOORS, ROOM_SIZE)
    loop.setUp()
    new_game = loop.start()
    if new_game:
        loop2 = GameLoop(ROOM_MAP_START, MAPS, DOORS, ROOM_SIZE)
        loop2.setUp()
        new_game = loop2.start()




if __name__ == "__main__":
    main()
