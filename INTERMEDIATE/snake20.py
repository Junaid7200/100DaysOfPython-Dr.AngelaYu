
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
import turtle as t
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for p in STARTING_POSITIONS:
            newS = t.Turtle("square")
            self.segments.append(newS)
            newS.color("white")
            newS.penup()
            newS.goto(p)
            
    def move(self):
            for seg in range(len(self.segments) - 1, 0, -1): # move the seg3 to position of seg2, seg2 to seg1 and so on
                new_x = self.segments[seg-1].xcor()  # get x coordinates of the segment that is ahead
                new_y = self.segments[seg-1].ycor()  # get y coordinates of the segment that is ahead
                self.segments[seg].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def add_segment(self, position):
        newS = t.Turtle("square")
        newS.color("white")
        newS.penup()
        newS.goto(position)
        self.segments.append(newS)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())