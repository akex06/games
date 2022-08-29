import pygame

from src.ball import Ball
from src.scenes import SceneManager
from src.player import Player

pygame.init()

def main_loop(game_controller: SceneManager, screen: pygame.Surface, clock: pygame.time.Clock):
    quit_game: bool = False

    while not quit_game:
        screen.fill(BLACK)
        quit_game = game_controller.process_game_interaction()

        scene = getattr(game_controller, game_controller.scene)()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    from src.constants import (
        BLACK,
        WIN_SIZE,
        FLAGS,
        PLAYER_HEIGHT,
        BALL_WIDTH,
        BALL_HEIGHT
    )

    screen = pygame.display.set_mode(WIN_SIZE, flags = FLAGS)
    clock = pygame.time.Clock()
    
    p_y = screen.get_height()/2-PLAYER_HEIGHT/2
    p1 = Player(screen, 20, p_y)
    p2 = Player(screen, screen.get_width()-40, p_y)
    ball = Ball(screen, screen.get_width()/2-BALL_WIDTH/2, screen.get_height()/2-BALL_HEIGHT/2)

    game_controller = SceneManager(screen, p1, p2, ball)

    main_loop(game_controller, screen, clock)