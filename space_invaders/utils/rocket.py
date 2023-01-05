import pygame

class Rocket:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.image = pygame.image.load("assets/cohete.png")
        self.width, self.height = self.image.get_width(), self.image.get_height()

        self.speed = 5

        self.x = self.screen.get_width() / 2 - self.image.get_width() / 2
        self.y = 500

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        self.screen.blit(self.image, (self.x, self.y))