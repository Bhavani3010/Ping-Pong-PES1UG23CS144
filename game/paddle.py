import pygame

class Paddle:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 10, 100)
        self.color = (255, 255, 255)
        self.speed = 10

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < self.screen.get_height():
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
