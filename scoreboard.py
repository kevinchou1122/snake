from sysconfig import get_path
from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align="center",font=("Ariel",24,"normal"))
        self.hideturtle()




    def game_over(self):

        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Ariel", 24, "normal"))
        self.hideturtle()
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Ariel", 24, "normal"))