# July 4, 2024


import turtle
import time
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height= 600)
screen.tracer(0)


import Paddle22 as p
import ball22
import score22

paddle1 = p.Paddle((350, 0))
paddle2 = p.Paddle((-350, 0))
ball = ball22.Ball()
scoreboards = score22.Scoreboard()
screen.update()

screen.listen()


screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")

screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboards.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboards.r_point()

screen.exitonclick()