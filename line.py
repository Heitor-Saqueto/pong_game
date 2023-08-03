from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("square")
        self.shapesize(stretch_wid=400, stretch_len=0.5)
