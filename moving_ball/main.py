import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball = Ball(WIDTH // 2, HEIGHT // 2, 25, WIDTH, HEIGHT)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move("LEFT")
            elif event.key == pygame.K_RIGHT:
                ball.move("RIGHT")
            elif event.key == pygame.K_UP:
                ball.move("UP")
            elif event.key == pygame.K_DOWN:
                ball.move("DOWN")

    screen.fill((255, 255, 255))
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)