import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
all_cars = []
num = 0
car = CarManager()
all_cars.append(car)
while game_is_on:
    time.sleep(0.1)
    screen.update()
    num += 1
    for each in all_cars:
        each.drive()
    if num % 6 == 0:
        new_car = CarManager()
        all_cars.append(new_car)


