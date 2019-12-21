import pygame
import sys
import math

pygame.init()
w, h = 400, 400
cx, cy = w//2, h//2

screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

while True:
    dt = clock.tick()/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        screen.fill((255, 255, 255))

        pygame.display.flip()
