import pygame

from src.ball import Ball

from src.constants import (
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    GREEN
)

class Player:
    def __init__(self, screen: pygame.Surface, x: int, y: int) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def update(self) -> None:
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, GREEN, self.rect)

    def iscoliding(self, ball: Ball) -> bool:
        if (ball.x <= self.x + self.width and ball.x >= self.x) or (ball.x+ball.width >= self.x and ball.x <= self.x):
            if (ball.y <= self.y + self.height and ball.y >= self.y) or (ball.y + ball.height >= self.y and ball.y <= self.y):
                return True