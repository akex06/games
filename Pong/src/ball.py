import pygame
import math
import random

from src.constants import (
    BALL_HEIGHT,
    BALL_SPEED,
    BALL_WIDTH,
    GREEN,
    PLAYER_SPEED
)

class Ball:
    def __init__(self, screen: pygame.Surface, x: int, y: int):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = BALL_WIDTH
        self.height = BALL_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.x_direction = -1
        self.y_direction = 1
        self.speed = BALL_SPEED
        self.B = random.randint(1, 30)+75

    def update(self):
        if self.win():
            exit()
                
        C = 90
        B = self.B
        A = 180 - C - B

        c = self.speed
        b = (c * math.sin(30))/math.sin(90)
        a =  (b * math.sin(A))/math.sin(B)

        self.x += b * self.x_direction
        self.y += a * self.y_direction

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, GREEN, self.rect)

    def win(self):
        if self.x <= 0:
            print("Player 2 wins")
            return True

        elif self.x >= self.screen.get_width():
            print("Player 1 wins")
            return True