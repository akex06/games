import pygame

from utils.rocket import Rocket
from utils.bullet import Bullet
from utils.aliens import Aliens

pygame.init()

flags = pygame.FULLSCREEN | pygame.RESIZABLE | pygame.SCALED
screen = pygame.display.set_mode((800, 600), flags = flags)
clock = pygame.time.Clock()

#   IMAGES
background = pygame.image.load("assets/fondo.png")

#   COHETE
rocket = Rocket(screen)

#   BALA
bullet = Bullet(screen)

#   ENEMIGO
aliens = Aliens(screen)

#   COLORS
BLACK = (0, 0, 0)

#   MÚSICA
pygame.mixer.Channel(0).play(pygame.mixer.Sound("assets/musica.mp3"))

quit_game: bool = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    screen.blit(background, (0, 0))
    
    rocket.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        bullet.shoot(rocket.x + rocket.width/2 - bullet.width/2, rocket.y - bullet.height)

    bullet.update()

    aliens.update(bullet)

    pygame.display.update()
    clock.tick(60)