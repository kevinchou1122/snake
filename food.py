from turtle import Turtle
import random
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def set_color(self):
        self.color(random.choice(rainbow_colors))

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)



