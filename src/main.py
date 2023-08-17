import pygame
from pygame.locals import *
from packages.consts import *

# pygame setup
pygame.init()

screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# game loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # clear last frame
    screen.fill("black")

    # RENDER GAME HERE

    # flip() display to put your work on screen
    pygame.display.flip()

    # max updates per second
    clock.tick(FPS)

pygame.quit()
