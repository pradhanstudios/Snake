import pygame
from pygame.locals import *
from packages.consts import *
from packages.player import *

# pygame setup
pygame.init()

# screen
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Snake")
# snake = Player(RESOLUTION[0]//2, RESOLUTION[1]//2, 100, 100, "black")

# clock
clock = pygame.time.Clock()
dt = 0  # initialize var for delta time

# font
font = pygame.font.SysFont("arial", 20)

# initialize game objects
board_g = pygame.Rect(BOARD_POS, BOARD_SIZE)
board = [[0] * NUM_COLS for _ in range(NUM_ROWS)]

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
    # snake.draw()

    # board background
    pygame.draw.rect(screen, "green", board_g, border_radius=5)
    pygame.draw.rect(screen, "black", board_g, 5, 5)

    # horizontal gridlines
    for x in range(
        board_g.left + (board_g.width // NUM_COLS),
        board_g.right,
        board_g.width // NUM_COLS,
    ):
        pygame.draw.line(screen, "black", (x, board_g.top), (x, board_g.bottom - 2), 3)

    # vertical gridlines
    for y in range(
        board_g.top + board_g.height // NUM_ROWS,
        board_g.bottom,
        board_g.height // NUM_ROWS,
    ):
        pygame.draw.line(screen, "black", (board_g.left, y), (board_g.right - 2, y), 3)

    # fps tracker
    fps_text = font.render(f"FPS: {round(clock.get_fps())}", True, "black")
    fps_text = font.render(f"FPS: {round(clock.get_fps())}", True, "black")
    fps_text_rect = fps_text.get_rect()
    fps_text_rect.center = (
        5 + (fps_text_rect.width // 2),
        5 + (fps_text_rect.height // 2),
    )
    screen.blit(fps_text, fps_text_rect)

    # flip() display to put your work on screen
    pygame.display.flip()

    # max updates per second
    dt = clock.tick(FPS) / 1000  # dt in seconds since last frame

pygame.quit()
