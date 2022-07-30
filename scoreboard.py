from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-270, 250)
        self.hideturtle()
        self.write(f"Level: {self.score}", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
