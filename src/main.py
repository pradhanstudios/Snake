import pygame
from pygame.locals import *
from packages.consts import *

# pygame setup
pygame.init()

screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
dt = 0  # initialize var for delta time

# initialize game objects
board = pygame.Rect(BOARD_POS, BOARD_SIZE)

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
    screen.fill("lightgreen")

    # RENDER GAME HERE

    # board
    pygame.draw.rect(screen, "green", board, border_radius=5)
    pygame.draw.rect(screen, "black", board, 5, 5)
    # horizontal gridlines
    for x in range(
        BOARD_POS[0] + BOARD_SIZE[0] // 20,
        BOARD_POS[0] + BOARD_SIZE[0],
        BOARD_SIZE[0] // 20,
    ):
        pygame.draw.line(
            screen, "black", (x, BOARD_POS[1]), (x, BOARD_POS[1] + BOARD_SIZE[1] - 2), 3
        )
    # vertical gridlines
    for y in range(
        BOARD_POS[1] + BOARD_SIZE[1] // 20,
        BOARD_POS[1] + BOARD_SIZE[1],
        BOARD_SIZE[1] // 20,
    ):
        pygame.draw.line(
            screen, "black", (BOARD_POS[0], y), (BOARD_POS[0] + BOARD_SIZE[0] - 2, y), 3
        )

    # flip() display to put your work on screen
    pygame.display.flip()

    # max updates per second
    dt = clock.tick(FPS) / 1000  # dt in seconds since last frame

pygame.quit()
