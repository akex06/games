import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

body = [[100, 100]]
head = body[0]
apple = []
score = 0

KEYS = {pygame.K_UP: [0, -50], pygame.K_DOWN: [0, 50], pygame.K_LEFT: [-50, 0], pygame.K_RIGHT: [50, 0]}

last_pressed = pygame.K_RIGHT

while True:
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key in KEYS:
                last_pressed = event.key


    x, y = KEYS[last_pressed]

    head[0] += x
    head[1] += y

    if head == apple:
        apple = []
        score += 1

    if not apple:
        apple = l = random.choice(random.choice([[[x*50, y*50] for x in range(10)] for y in [x for x in range(10)]]))
    print(apple)
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(apple[0], apple[1], 50, 50))

    if head[0] > 500 or head[0] < 0 or head[1] > 500 or head[1] < 0:
        print(f"You lost, your score was of {score}")
        exit()

    p = pygame.Rect(head[0], head[1], 50, 50)
    pygame.draw.rect(screen, (255, 0, 0), p)

    pygame.display.update()
    clock.tick(2)