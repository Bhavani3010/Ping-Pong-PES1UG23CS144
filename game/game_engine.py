import pygame
from .ball import Ball
from .paddle import Paddle

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.player_paddle = Paddle(screen, 20, self.screen_height // 2 - 50)
        self.ai_paddle = Paddle(screen, self.screen_width - 30, self.screen_height // 2 - 50)
        self.ball = Ball(screen, self.player_paddle, self.ai_paddle)
        self.player_score = 0
        self.ai_score = 0
        self.winning_score = 5
        self.font = pygame.font.Font(None, 36)

    def reset_game(self):
        self.ball.reset_position()
        self.player_paddle.rect.y = self.screen_height // 2 - 50
        self.ai_paddle.rect.y = self.screen_height // 2 - 50
        self.player_score = 0
        self.ai_score = 0

    def move_ai(self):
        if self.ai_paddle.rect.centery < self.ball.rect.centery:
            self.ai_paddle.move_down()
        elif self.ai_paddle.rect.centery > self.ball.rect.centery:
            self.ai_paddle.move_up()

    def check_game_over(self):
        if self.player_score >= self.winning_score:
            self.display_winner("Player Wins!")
            return True
        elif self.ai_score >= self.winning_score:
            self.display_winner("AI Wins!")
            return True
        return False

    def display_winner(self, text):
        render_text = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(render_text, (self.screen_width // 2 - render_text.get_width() // 2,
                                       self.screen_height // 2 - render_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(3000)

    def start_menu(self):
        self.screen.fill((0, 0, 0))
        options = ["Press 3 for Best of 3", "Press 5 for Best of 5", "Press 7 for Best of 7", "ESC to Exit"]
        for i, option in enumerate(options):
            render_text = self.font.render(option, True, (255, 255, 255))
            self.screen.blit(render_text, (50, 100 + i * 80))
        pygame.display.flip()

        selected = False
        while not selected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        self.winning_score = 3
                        selected = True
                    elif event.key == pygame.K_5:
                        self.winning_score = 5
                        selected = True
                    elif event.key == pygame.K_7:
                        self.winning_score = 7
                        selected = True
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
        self.reset_game()

    def replay_option(self):
        self.start_menu()

    def draw(self):
        self.player_paddle.draw()
        self.ai_paddle.draw()
        self.ball.draw()
        self.display_score()

    def display_score(self):
        player_score_text = self.font.render(str(self.player_score), True, (255, 255, 255))
        ai_score_text = self.font.render(str(self.ai_score), True, (255, 255, 255))
        self.screen.blit(player_score_text, (self.screen_width // 4 - player_score_text.get_width() // 2, 20))
        self.screen.blit(ai_score_text, (3 * self.screen_width // 4 - ai_score_text.get_width() // 2, 20))

    def update_score(self):
        if self.ball.rect.left <= 0:
            self.ai_score += 1
            self.ball.reset_position()
        elif self.ball.rect.right >= self.screen_width:
            self.player_score += 1
            self.ball.reset_position()
