import pygame
from packages.consts import *

# initialize engine
pygame.init()

screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Snake")

# set max FPS
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear the screen
    screen.fill(BLACK)

    # max updates per second
    clock.tick(FPS)

pygame.quit()
