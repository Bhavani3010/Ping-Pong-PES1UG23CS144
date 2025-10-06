import pygame
from game.game_engine import GameEngine

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ping Pong Game")
    clock = pygame.time.Clock()

    game = GameEngine(screen)
    game.start_menu()

    running = True
    while running:
        screen.fill((0, 0, 0))

        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Player input ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            game.player_paddle.move_up()
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            game.player_paddle.move_down()

        # --- Game logic ---
        game.move_ai()
        game.ball.move()
        game.draw()
        game.update_score()

        if game.check_game_over():
            game.replay_option()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
