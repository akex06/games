import pygame

from typing import Optional
from utils.bullet import Bullet

class Alien:
    def __init__(self, screen: pygame.Surface, x: int, y: int, *, speed: int = 5) -> None:
        self.screen = screen
        self.image = pygame.image.load("assets/enemigo.png")
        self.rect = self.image.get_rect()
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.x = x
        self.y = y
        self.direction = -1
        self.speed = speed
        self.side = "left"

    def change_line(self):
        self.y += self.image.get_height() + 20
        self.direction *= -1
        self.x += self.speed * self.direction
        self.side = "right" if self.side == "left" else "left"
    
    def update(self):
        self.x += self.speed * self.direction

        left, right = self.x <= self.image.get_width(), self.x >= self.screen.get_width() - self.image.get_width()
        if any(
            (
                self.side == "left" and left,
                self.side == "right" and right
            )
        ):
            self.change_line()

        self.rect.x = self.x
        self.rect.y = self.y

        self.screen.blit(self.image, self.rect.topleft)

class Aliens:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.image = pygame.image.load("assets/enemigo.png")
        self.aliens: list[Alien] = []
        self.rounds = 1

        self.generate_aliens()

    def generate_aliens(self):
        for i in range(self.rounds):
            self.aliens.append(
                Alien(
                    self.screen,
                    self.screen.get_width() + self.image.get_width() * i + 20 * i,
                    0
                )
            )

    def update(self, bullet: Bullet):
        for alien in self.aliens:
            alien.update()

            if bullet.x >= alien.x and \
                bullet.x + bullet.width <= alien.x + alien.width and \
                bullet.y >= alien.y and \
                bullet.y + bullet.height <= alien.y + alien.height:

                pygame.mixer.Channel(2).play(pygame.mixer.Sound("assets/golpe.mp3"))

                self.aliens.remove(alien)

        if len(self.aliens) == 0:
            self.rounds += 1
            self.generate_aliens()

        if any(filter(lambda alien: alien.y >= 500, self.aliens)):
            print(f"Has perdido! Has hecho {self.rounds - 1} rondas")
            exit()