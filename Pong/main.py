import pygame

pygame.init()

flags = pygame.FULLSCREEN | pygame.SCALED
screen = pygame.display.set_mode((700, 700), flags = flags)
clock = pygame.time.Clock()

p1_width, p1_height = 20, 200

p1_x = 20
p1_y = screen.get_height()/2-p1_height/2


p2_width, p2_height = 20, 200

p2_x = screen.get_width() - p2_width*2
p2_y = screen.get_height()/2-p2_height/2

player_speed = 5

#   COLORS
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(BLACK)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1_y -= player_speed

    if keys[pygame.K_s]:
        p1_y += player_speed

    if keys[pygame.K_UP]:
        p2_y -= player_speed

    if keys[pygame.K_DOWN]:
        p2_y += player_speed
    
    p1 = pygame.Rect(p1_x, p1_y, p1_width, p1_height)
    p2 = pygame.Rect(p2_x, p2_y, p2_width, p2_height)

    pygame.draw.rect(screen, GREEN, p1)
    pygame.draw.rect(screen, GREEN, p2)

    pygame.display.update()
    clock.tick(60)