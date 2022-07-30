import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
num = 0
car = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    num += 1
    car.drive()
    if num % 6 == 0:
        car.create_car()

    if player.ycor() > 280:
        pass
#       add a level, reset position, speed up cars



