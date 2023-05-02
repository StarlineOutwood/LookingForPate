import os
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)

from sprites.laudna import Laudna
from sprites.pate import Pate
from room import Room
from sprites.door import Door

ROOM_MAP_START = [[3, 3, 3, 3, 3, 3, 3],
                  [4, 1, 0, 0, 0, 0, 4],
                  [4, 0, 0, 0, 0, 0, 4],
                  [4, 0, 0, 0, 0, 0, 5],
                  [3, 3, 3, 3, 3, 5, 3]]

ROOM_MAP_0 = [[3, 3, 3, 3, 3, 3, 3],
              [4, 0, 0, 0, 0, 0, 5],
              [4, 0, 0, 0, 0, 0, 4],
              [4, 0, 0, 0, 0, 0, 4],
              [3, 3, 3, 3, 3, 5, 3]]

ROOM_MAP_1 = [[3, 3, 3, 3, 3, 3, 3],
              [5, 0, 4, 0, 4, 0, 5],
              [4, 0, 4, 0, 0, 0, 4],
              [4, 0, 0, 0, 4, 0, 4],
              [3, 3, 3, 3, 3, 5, 3]]

ROOM_MAP_2 = [[3, 3, 3, 3, 3, 3, 3],
              [5, 0, 0, 0, 0, 0, 4],
              [4, 0, 0, 0, 0, 0, 4],
              [4, 0, 0, 0, 0, 2, 4],
              [3, 3, 3, 3, 3, 3, 3]]

ROOM_MAP_3 = [[3, 3, 3, 3, 3, 5, 3],
              [4, 0, 0, 4, 0, 0, 4],
              [4, 0, 0, 4, 0, 0, 4],
              [4, 0, 0, 4, 0, 0, 5],
              [3, 3, 3, 3, 3, 3, 3]]

ROOM_MAP_4 = [[3, 3, 3, 3, 3, 5, 3],
              [4, 0, 0, 0, 0, 0, 4],
              [4, 0, 0, 4, 0, 0, 4],
              [5, 0, 0, 4, 0, 0, 4],
              [3, 3, 3, 3, 3, 3, 3]]

MAPS = [ROOM_MAP_0, ROOM_MAP_1, ROOM_MAP_2, ROOM_MAP_3, ROOM_MAP_4]

DOORS = [[1, 3], [0, 2, 4], [1], [0, 4], [1, 3]]

ROOM_SIZE = 200


class GameLoop():
    """Class where we run different game loops, aka "states"

    Attributes:
        only itself
    """

    def __init__(self, start_map, maps, doors, room_size):
        self.start_map = start_map
        self.maps = maps
        self.doors = doors
        self.room_size = room_size
        self.cookies = 0
        return

    def setUp(self):

        ROOM_MAP_0 =[[3, 3, 3, 3, 3, 3, 3, 3, 3],
                    [4, 1, 0, 0, 0, 0, 0, 0, 5],
                    [4, 0, 0, 0, 0, 0, 0, 0, 4],
                    [4, 0, 0, 0, 0, 0, 0, 0, 4],
                    [4, 0, 0, 0, 0, 0, 0, 0, 4],
                    [3, 3, 3, 3, 3, 5, 3, 3, 3]]

        ROOM_MAP_1 =[[3, 3, 3, 3, 3, 3, 3, 3, 3],
                    [5, 0, 4, 6, 0, 0, 0, 0, 4],
                    [4, 0, 4, 4, 4, 0, 4, 0, 4],
                    [4, 0, 0, 0, 4, 0, 4, 0, 4],
                    [4, 0, 4, 0, 0, 0, 4, 0, 5],
                    [3, 3, 3, 3, 5, 3, 3, 3, 3]]

        ROOM_MAP_2 =[[3, 3, 3, 3, 3, 3, 3, 3, 3],
                    [4, 0, 4, 2, 0, 0, 0, 6, 4],
                    [4, 0, 4, 4, 4, 0, 0, 0, 4],
                    [4, 0, 0, 0, 4, 0, 0, 0, 4],
                    [5, 0, 0, 0, 0, 0, 0, 6, 4],
                    [3, 3, 3, 3, 3, 3, 3, 3, 3]]

        ROOM_MAP_3 =[[3, 3, 3, 3, 3, 5, 3, 3, 3],
                    [4, 0, 4, 0, 0, 0, 0, 6, 4],
                    [4, 0, 4, 4, 0, 0, 0, 0, 4],
                    [4, 0, 0, 4, 0, 0, 0, 0, 4],
                    [4, 0, 0, 4, 0, 0, 0, 6, 5],
                    [3, 3, 3, 3, 3, 3, 3, 3, 3]]

        ROOM_MAP_4 =[[3, 3, 3, 3, 5, 3, 3, 3, 3],
                    [4, 4, 0, 0, 0, 0, 0, 6, 4],
                    [4, 0, 0, 4, 0, 0, 0, 0, 4],
                    [4, 0, 4, 4, 0, 0, 0, 0, 4],
                    [5, 0, 4, 6, 0, 0, 0, 6, 4],
                    [3, 3, 3, 3, 3, 3, 3, 3, 3]]

        self.maps = [ROOM_MAP_0, ROOM_MAP_1, ROOM_MAP_2, ROOM_MAP_3, ROOM_MAP_4]

        self.doors = [[1, 3], [0, 2, 4], [1], [0, 4], [1, 3]]

        self.room_size = 150

        self.start_map = ROOM_MAP_0
    
    def start(self):
        height = len(self.start_map)
        width = len(self.start_map[0])
        dis_height = height*self.room_size
        dis_width = width*self.room_size
        screen = pygame.display.set_mode((dis_width, dis_height))
        room = Room(self.room_size, self.start_map, self.doors[0])
        pygame.init()
        room.all_sprites.draw(screen)
        room.Laudna.draw(screen)

        generating = True
        end = False
        while generating:
            door = self.loop(room, screen)
            if door is None:
                generating = False
                end = True
                return self.end(end)
            else:
                next = door.next_room
                x = door.px
                y = door.py
                new_map = self.prep_map(self.maps[next], x, y)
            screen = pygame.display.set_mode((dis_width, dis_height))
            room = Room(self.room_size, new_map, self.doors[next])
            pygame.init()
            room.all_sprites.draw(screen)
            room.Laudna.draw(screen)

    def loop(self, room, screen):
        """The actual game is running, were able to play

        Args:
            room: what room we're playing in right now
            screen: the screen where the game is drawn
         """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        return
                elif event.type == QUIT:
                    running = False

            pressed_keys = pygame.key.get_pressed()
            self.move(room, pressed_keys, screen)
            if room.Pate is not None:
                if self.collision_pate(room, screen):
                    return
            for cookie in room.cookies:
                if room.Laudna.colliding_cookie(cookie):
                    self.eat_cookie(cookie, room)
            for door in room.Doors:
                if room.Laudna.colliding_Door(door):
                    return door

    def collision_pate(self, room, screen):
        if not room.Laudna.colliding_Pate(room.Pate):
            dirname = os.path.dirname(__file__)
            end = pygame.image.load(
                os.path.join(dirname, "End_screen.PNG"))
            end = pygame.transform.scale(end, (1000, 500))
            screen.blit(end, (200, 200))
            pygame.display.flip()
            return True

    def move(self, room, pressed_keys, screen):
        room.Laudna.move(pressed_keys, room.walls_H, room.walls_V)
        screen.fill((0, 0, 0))
        screen.blit(room.Laudna.image, room.Laudna.rect)
        room.all_sprites.draw(screen)
        largeFont = pygame.font.SysFont('eufm10', 30)
        text = largeFont.render('Collected Cookies: ' + str(self.cookies), 1, (255,255,255))
        screen.blit(text, (21, 31))
        text = largeFont.render('Collected Cookies: ' + str(self.cookies), 1, (0,0,0))
        screen.blit(text, (20, 30))
        pygame.display.flip()
                
    def eat_cookie(self, cookie, room):
        room.map[cookie.py][cookie.px] = 0
        self.cookies += 1
        cookie.eat() 

    def prep_map(self, new_map, x, y):
        for i in range(len(new_map)):
            for j in range(len(new_map[0])):
                if new_map[i][j] == 1:
                    new_map[i][j] = 0 
        if x == 0:
            new_map[y][5] = 1
        elif x == 8:
            new_map[y][1] = 1
        elif y == 0:
            new_map[4][x] = 1
        elif y == 5:
            new_map[1][x] = 1  
        return new_map   

    def end(self, end=True):
        """We are at the end and waiting for the player t decide if they want to playa again or not

        Args:
            end: are we actively in the end or not
         """
        while end:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    end = False
                    return False

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        end = False
                        return False
                    if event.key == K_SPACE:
                        end = False
                        return True
                elif event.type == QUIT:
                    end = False
