import turtle as t
import random as r
class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(x = r.randint(-280, 280), y = r.randint(-280, 280))

    def refresh(self):
        self.goto(x = r.randint(-280, 280), y = r.randint(-280,280))