COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 10
import random as r 
import turtle as t
class CarManager(t.Turtle):
        def __init__(self):
            self.all_cars = []
            self.car_speed = STARTING_MOVE_DISTANCE

        def create_cars(self):
            random_chance = r.randint(1,6)
            if random_chance == 1:
                new_car = t.Turtle("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.penup()
                new_car.color(r.choice(COLORS))
                new_car.goto(300, r.randint(-250, 250))
                self.all_cars.append(new_car)
        def move_cars(self):
            for car in self.all_cars:
                car.backward(self.car_speed)
        def level_up(self):
            self.car_speed += MOVE_INCREMENT