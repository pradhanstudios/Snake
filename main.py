import pygame

BLACK = (0, 0, 0)

# initialize engine
pygame.init()

screen = pygame.display.set_mode((1200, 800))
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
    clock.tick(60)

pygame.quit()
