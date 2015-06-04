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
    global ball_velocity
    x, y = ball_velocity
    ball.left += x
    ball.top += y

    # Bounce
    if ball.right > WIDTH:
        displacement = ball.right - WIDTH
        ball.right -= displacement
        ball_velocity = (ball_velocity[0] * -1,
                         ball_velocity[1])
    if ball.left < 0:
        displacement = 0 - ball.left
        ball.left += displacement
        ball_velocity = (ball_velocity[0] * -1,
                         ball_velocity[1])
    if ball.bottom > HEIGHT:
        displacement = ball.bottom - HEIGHT
        ball.bottom -= displacement
        ball_velocity = (ball_velocity[0],
                         ball_velocity[1] * -1)
    if ball.top < 0:
        displacement = 0 - ball.top
        ball.top += displacement
        ball_velocity = (ball_velocity[0],
                         ball_velocity[1] * -1)

    # paddle collision
    if (ball.left < left_paddle.right and 
       ball.top > left_paddle.top and
       ball.bottom < left_paddle.bottom):
        displacement = left_paddle.right - ball.left
        ball.left += displacement
        ball_velocity = (ball_velocity[0] * -1,
                         ball_velocity[1])
        


def on_key_down(key):
    if key == keys.UP:
        left_paddle.top -= 10
    if key == keys.DOWN:
        left_paddle.top += 10
