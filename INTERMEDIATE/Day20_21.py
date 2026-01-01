# July 4, 2024

# snake game
# create snake body
# move continuously
# control the snake
# put food on screen
# eat food
# add score
# when the game should end

import turtle as t 
import time
import scoreboard21
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width= 600, height = 600)
screen.title("The Snake Game")
screen.tracer(0)


import snake20 as s
import food21 as f
snake = s.Snake()
food = f.Food()
scoreBoard = scoreboard21.Scoreboard()
screen.listen()

screen.onkey(fun = snake.up, key = "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor()  < -280:
        #game_on = False
        scoreBoard.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            scoreBoard.reset()
            snake.reset()




screen.exitonclick()

