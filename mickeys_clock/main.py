import pygame
import sys
import time
from clock import Clock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey_clock = Clock(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    mickey_clock.update()

    pygame.display.flip()
    clock.tick(60)