import pygame

class Ball:
    def __init__(self, screen, player_paddle, ai_paddle):
        self.screen = screen
        self.player_paddle = player_paddle
        self.ai_paddle = ai_paddle
        self.rect = pygame.Rect(screen.get_width() // 2 - 15, screen.get_height() // 2 - 15, 30, 30)
        self.color = (255, 255, 255)
        self.velocity_x = 5
        self.velocity_y = 5

    def move(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.velocity_y *= -1

        if self.rect.colliderect(self.player_paddle.rect) or self.rect.colliderect(self.ai_paddle.rect):
            self.velocity_x *= -1

    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, self.rect)

    def reset_position(self):
        self.rect.center = self.screen.get_rect().center
        self.velocity_x *= -1
