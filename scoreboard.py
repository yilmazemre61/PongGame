from turtle import Turtle

FONT = ("Arial", 50, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x= 0, y= 250)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_lscore(self):
        self.l_score += 1

    def update_rscore(self):
        self.r_score += 1

    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}          {self.r_score}", align=ALIGNMENT, font=FONT)
