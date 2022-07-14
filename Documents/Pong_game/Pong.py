import pygame, sys, random
from Ball import Ball
from Paddle import Paddle

# General setup
pygame.init()
clock = pygame.time.Clock()

# Display surface
screen_width, screen_height = 1200, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Rectangles
ball = Ball(screen_width/2 - 14, screen_height/2 - 14, 28, 28)
player = Paddle(10, screen_height/2 - 100)
opponent = Paddle(screen_width - 20, screen_height/2 - 100)

# Colors
bg_color = pygame.Color('grey12')
white, grey = (255, 255, 255), (150, 150, 150)

# Font & score
font = pygame.font.SysFont("Arial", 40)
player_score = 0
opponent_score = 0

def check_scored():
    """Update the score"""
    global player_score, opponent_score
    if ball.ball.right >= screen_width-5:
        player_score += 1
    if ball.ball.left <= 5:
        opponent_score += 1

# Timer
start_time = None
def start_timer():
    """Set the ball in the middle of the screen"""
    global start_time
    if ball.ball.left <= 5 or ball.ball.right >= screen_width-5:
        start_time = pygame.time.get_ticks()

def restart():
    """Manage the timer"""
    global end_time, start_time
    end_time = pygame.time.get_ticks()
    ball.ball.topleft = (screen_width/2 - ball.width/2, screen_height/2 - ball.height/2)
    ball.speed_y, ball.speed_x = 0, 0

    if end_time - start_time < 1000:
        three = font.render("3", False, grey)
        screen.blit(three, (screen_width/2-9, screen_height/2+35))
    elif 1000 < end_time - start_time < 2000:
        two = font.render("2", False, grey)
        screen.blit(two, (screen_width/2-9, screen_height/2+35))
    elif 2000 < end_time - start_time < 3000:
        one = font.render("1", False, grey)
        screen.blit(one, (screen_width/2-9, screen_height/2+35))
    else:
        ball.speed_x = 7 * random.choice([-1,1])
        ball.speed_y = 7 * random.choice([-1,1])
        start_time = None

# Main game loop
while True:
    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Color window
    screen.fill(bg_color)

    # Draw ball and paddles
    pygame.draw.aaline(screen, grey, (screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.ellipse(screen, grey, ball.ball)
    pygame.draw.rect(screen, grey, player.paddle)
    pygame.draw.rect(screen, grey, opponent.paddle)

    p_score = font.render(f"{player_score}", False, grey)
    o_score = font.render(f"{opponent_score}", False, grey)
    screen.blit(p_score, (screen_width/2 - 35, screen_height/2-20))
    screen.blit(o_score, (screen_width/2 + 15, screen_height/2-20))

    # Game logic
    ball.move()
    check_scored()
    ball.check_collision(player)
    ball.check_collision(opponent)

    player.move('player')
    opponent.move('opponent')

    #Timer
    start_timer()
    if start_time:
        restart()


    # Redraw window
    pygame.display.flip()
    clock.tick(60)
