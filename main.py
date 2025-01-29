import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
line = Line()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

def go_to():
    r_paddle.goto(x=350, y=0)
    l_paddle.goto(x=-350, y=0)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Collision With the Top and Bottom Wall and Bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # Collision with the Paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()
    # Detect when paddle misses
    if ball.xcor() > 350:
        scoreboard.update_lscore()
        scoreboard.update_score()
        ball.reset_position()
        go_to()
    elif ball.xcor() < -350:
        scoreboard.update_rscore()
        scoreboard.update_score()
        ball.reset_position()
        go_to()















































screen.exitonclick()