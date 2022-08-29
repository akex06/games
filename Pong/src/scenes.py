import pygame

from src.player import Player
from src.ball import Ball

from src.constants import (
    BALL_HEIGHT,
    BALL_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_SPEED,
    PLAYER_WIDTH
)

class SceneManager:
    def __init__(self, screen: pygame.Surface, p1: Player, p2: Player, ball: Ball):
        self.screen = screen
        self.scene = "game"
        self.p1 = p1
        self.p2 = p2
        self.ball = ball

    def process_game_interaction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def game(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.p1.y -= PLAYER_SPEED

        if keys[pygame.K_s]:
            self.p1.y += PLAYER_SPEED

        if keys[pygame.K_UP]:
            self.p2.y -= PLAYER_SPEED

        if keys[pygame.K_DOWN]:
            self.p2.y += PLAYER_SPEED

        if self.p2.y <= 0:
            self.p2.y = 0

        elif self.p2.y >= self.screen.get_height()-PLAYER_HEIGHT:
            self.p2.y = self.screen.get_height()-PLAYER_HEIGHT

        if self.p1.y <= 0:
            self.p1.y = 0

        elif self.p1.y >= self.screen.get_height()-PLAYER_HEIGHT:
            self.p1.y = self.screen.get_height()-PLAYER_HEIGHT

        for player in (self.p1, self.p2):
            if player.iscoliding(self.ball):
                self.ball.x_direction *= -1
                self.ball.speed += 0.5

        if self.ball.y <= 0 or self.ball.y >= self.screen.get_height()-BALL_HEIGHT:
            self.ball.y_direction *= -1

        self.p1.update()
        self.p2.update()
        self.ball.update()