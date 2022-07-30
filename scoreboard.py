from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-270, 250)
        self.color("black")
        self.hideturtle()
        self.write(f"Level: {self.score}", font=FONT)
