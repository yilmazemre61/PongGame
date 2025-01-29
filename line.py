from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=0, y=300)
        self.color("white")
        self.setheading(270)
        self.draw_line()


    def draw_line(self):
        for _ in range(12):
            self.forward(30)
            self.penup()
            self.forward(20)
            self.pendown()