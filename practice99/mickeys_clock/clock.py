import pygame
import time
import math

class Clock:
    def __init__(self, screen):
        self.screen = screen

        self.center = (300, 300)

        self.hand_img = pygame.image.load("images/mickey_hand.png")
        self.hand_img = pygame.transform.scale(self.hand_img, (200, 20))

    def draw_hand(self, image, angle, length):
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect(center=self.center)
        self.screen.blit(rotated, rect)

    def update(self):
        t = time.localtime()
        seconds = t.tm_sec
        minutes = t.tm_min

        # angles
        sec_angle = -seconds * 6
        min_angle = -minutes * 6

        self.draw_hand(self.hand_img, sec_angle, 200)
        self.draw_hand(self.hand_img, min_angle, 200)
