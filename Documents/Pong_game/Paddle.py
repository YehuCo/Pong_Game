import pygame

# Initialize pygame
pygame.init()

# Display screen variables
screen_width = 1200
screen_height = 700

class Paddle():
    """Player paddle and opponent paddle"""

    def __init__(self, x_topleft_start, y_topleft_start):
        """Initialize paddle attributes"""
        self.paddle = pygame.Rect(x_topleft_start, y_topleft_start, 10, 150)
        self.y_speed = 7
        self.score = 0

    def check_borders(self):
        "Keep paddle on the screen"
        if self.paddle.top <= 5:
            self.paddle.top = 5
        if self.paddle.bottom >= screen_height-5:
            self.paddle.bottom = screen_height-5

    def move(self, paddle):
        """Move the paddle"""
        keys = pygame.key.get_pressed()
        if paddle == 'opponent':
            if keys[pygame.K_UP]:
                self.paddle.top -= 6
            if keys[pygame.K_DOWN]:
                self.paddle.bottom += 6
                
        if paddle == 'player':
            if keys[pygame.K_w]:
                self.paddle.top -= 6
            if keys[pygame.K_s]:
                self.paddle.bottom += 6

        self.check_borders()
