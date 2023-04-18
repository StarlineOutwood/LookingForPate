import os
import pygame
from sprites.Laudna import Laudna
from sprites.Pate import Pate
from Room import Room

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

ROOM_MAP = [[3, 3, 3, 3, 3, 3, 3],
            [4, 0, 0, 0, 0, 0, 4],
            [4, 2, 0, 0, 0, 1, 4],
            [4, 0, 0, 0, 0, 0, 4],
            [3, 3, 3, 3, 3, 3, 3]]

ROOM_SIZE = 200

def main():
    height = len(ROOM_MAP)
    width = len(ROOM_MAP[0])
    dis_height = height*ROOM_SIZE
    dis_width = width*ROOM_SIZE
    room = Room(ROOM_SIZE, ROOM_MAP)
    screen = pygame.display.set_mode((dis_width, dis_height))
    room = Room(ROOM_SIZE, ROOM_MAP)
    pygame.init()
    room.all_sprites.draw(screen)
    room.Laudna.draw(screen)

    running = True
    end = False

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
        if not room.Laudna.colliding_Pate(room.Pate):
            dirname = os.path.dirname(__file__)
            end = pygame.image.load(os.path.join(dirname, "End_screen.PNG"))
            end = pygame.transform.scale(end, (1000, 500))
            screen.blit(end, (200, 200))
            pygame.display.flip()
            running = False
            end = True
    
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    end = False           
            elif event.type == QUIT:
                end = False
        


if __name__ == "__main__":
    main()

