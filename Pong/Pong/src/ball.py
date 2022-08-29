import pygame

from src.constants import (
    BALL_HEIGHT,
    BALL_SPEED,
    BALL_WIDTH,
    GREEN
)

class Ball:
    def __init__(self, screen: pygame.Surface, x: int, y: int):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = BALL_WIDTH
        self.height = BALL_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = -1
        self.speed = BALL_SPEED * self.direction

    def update(self):
        if self.x <= 0:
            print("Player 2 wins")
            exit()

        elif self.x >= self.screen.get_width():
            print("Player 1 wins")
            exit()

        
        self.x += self.speed * self.direction
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, GREEN, self.rect)