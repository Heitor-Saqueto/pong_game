from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
        self.goto(-100, 200)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
