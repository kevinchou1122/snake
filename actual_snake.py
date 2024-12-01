import time
from turtle import Turtle,Screen
coords=[(0,0),(-20,0),(-40,0)]
move_distance=20
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snakes=[]
        self.game_on=True
    def create(self):
        for i in coords:
           self.add_segment(i)

    def add_segment(self,position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snakes.append(segment)
    def extend(self):
        self.add_segment(self.snakes[-1].position())
    def move(self):
        for seg in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg - 1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.snakes[0].forward(move_distance)

    def up(self):
        if self.snakes[0].heading()!= 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading()!= 90:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def reset(self):
        # Remove all existing segments
        for segment in self.snakes:
            segment.hideturtle()  # Hide the turtle object
        self.snakes.clear()  # Clear the list to release memory
        self.create()  # Recreate the initial snake







