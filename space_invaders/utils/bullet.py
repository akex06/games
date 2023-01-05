import pygame

class Bullet:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.image = pygame.image.load("assets/bala.png")
        self.rect = self.image.get_rect()
        self.width, self.height = self.image.get_width(), self.image.get_height()

        self.x = -1
        self.y = -1
        
        self.shooted = False

        self.speed = 10

    def update(self) -> None:
        if self.shooted:
            self.y -= self.speed
            self.screen.blit(self.image, (self.x, self.y))

            if self.y + self.image.get_height() <= 0:
                self.shooted = False

        self.rect = self.image.get_rect()

    def shoot(self, x: int, y: int) -> bool:
        if self.shooted:
            return False

        pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/disparo.mp3"))

        self.shooted = True
        self.x = x
        self.y = y

        return True