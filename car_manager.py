from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        random_y = random.randint(-250, 250)
        self.goto(290, random_y)
        self.speed = STARTING_MOVE_DISTANCE
        self.drive()

    def drive(self):
        if self.xcor() > -320:
            self.forward(self.speed)

