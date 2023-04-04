import pygame
from sprites.Laudna import Laudna
from sprites.Pate import Pate

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

laudna = Laudna()
pate = Pate()

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
    laudna.move(pressed_keys)
    screen.fill((100, 100, 100))
    screen.blit(laudna.image, laudna.rect)
    screen.blit(pate.image, pate.rect)    
    pygame.display.flip()

