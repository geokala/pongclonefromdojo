import random

WIDTH = 800
HEIGHT = 600

left_paddle = Rect((0,0), (20,70))
left_paddle.left += 50
left_paddle.top += 50
ball = Rect( (0,0), (25,25) )
ball.top = WIDTH / 2 - ball.width / 2
ball.right = HEIGHT / 2 - ball.height / 2
ball_velocity = (random.choice([-3,3]), random.choice(range(-2,2)))

colour = (200,0,0)
ball_colour = (100, 150, 50)

def draw():
    screen.clear()
    screen.draw.filled_rect(left_paddle, colour)
    screen.draw.filled_rect(ball, ball_colour)

def update():
    x, y = ball_velocity
    ball.left += x
    ball.top += y

def on_key_down(key):
    if key == keys.UP:
        box.top -= 2
    if key == keys.DOWN:
        box.top += 2
