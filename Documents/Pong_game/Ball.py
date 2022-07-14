import pygame
from Paddle import Paddle

# Initialize pygame
pygame.init()

# Display screen variables
screen_width = 1200
screen_height = 700

class Ball():
    """Ball object"""

    def __init__(self, x_start, y_start, width, height):
        """Initialize ball object attributes"""
        self.speed_y = 7
        self.speed_x = 7
        self.ball = pygame.Rect(x_start, y_start, width, height)
        self.width = width
        self.height = height

    def move(self):
        """Check for collision with screen borders"""
        self.ball.right += self.speed_x
        self.ball.top += self.speed_y

        if self.ball.right >= screen_width:
             self.ball.topleft = (screen_width/2 - self.width/2, screen_height/2 - self.height/2)
        if self.ball.left <= 3:
            self.ball.topleft = (screen_width/2 - self.width/2, screen_height/2 - self.height/2)
        if self.ball.top <= 3:
            self.speed_y *= -1
        if self.ball.bottom >= screen_height:
            self.speed_y *= -1


    def check_collision(self, player):
        """Check for collision with paddles"""
        if self.ball.colliderect(player.paddle):
            if abs(self.ball.top - player.paddle.bottom) < 10 and self.speed_y < 0:
                self.speed_y *= -1
            if abs(self.ball.bottom - player.paddle.top) < 10 and self.speed_y > 0:
                self.speed_y *= -1
            if abs(self.ball.right - player.paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.ball.left - player.paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
