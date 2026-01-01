# July 4, 2024

# event listeners



# def move_Fowards():
#     tim.forward(10)

# def move_Backwards():
#     tim.backward(10)

# def move_counterClockwise():
#     tim.left(10)
#     tim.forward(10)

# def move_Clockwise():
#     tim.right(10)
#     tim.forward(10)

# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(key = "w", fun = move_Fowards)
# screen.onkey(key = "s", fun = move_Backwards)
# screen.onkey(key = "a", fun = move_counterClockwise)
# screen.onkey(key = "d", fun = move_Clockwise)
# screen.onkey(key = "c", fun = clear_screen)


# turtle race:
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()



# passing a function into another function as an args (higher order function, calc is a higher order function because it is taking another function, can't do this in most other languages )
# def add(n1, n2):
#     return n1 + n2

# def calc(n1, n2, func):
#     print (func(n1, n2))
#     return func(n1, n2)

# calc(5, 10, add)

