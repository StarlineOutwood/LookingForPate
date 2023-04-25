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


class GameLoop():

    def __init__(self):
        return

    def start(self, room, screen):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

            pressed_keys = pygame.key.get_pressed()
            room.Laudna.move(pressed_keys, room.walls_H, room.walls_V)
            screen.fill((0, 0, 0))
            screen.blit(room.Laudna.image, room.Laudna.rect)
            room.all_sprites.draw(screen)
            pygame.display.flip()
            if room.Pate is not None:
                if not room.Laudna.colliding_Pate(room.Pate):
                    dirname = os.path.dirname(__file__)
                    end = pygame.image.load(
                        os.path.join(dirname, "End_screen.PNG"))
                    end = pygame.transform.scale(end, (1000, 500))
                    screen.blit(end, (200, 200))
                    pygame.display.flip()
                    return
            for door in room.Doors:
                if room.Laudna.colliding_Door(door):
                    return door.next()

    def end(self, end=True):
        while end:
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    end = False

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        end = False
                    if event.key == K_SPACE:
                        end = False
                        return True
                elif event.type == QUIT:
                    end = False
