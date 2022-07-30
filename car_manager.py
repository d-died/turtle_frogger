from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.create_car()

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.setheading(180)
        random_y = random.randint(-250, 250)
        new_car.goto(290, random_y)
        new_car.speed = STARTING_MOVE_DISTANCE
        self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

