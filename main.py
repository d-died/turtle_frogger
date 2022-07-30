import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_mgmt = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
num = 0
while game_on:
    time.sleep(0.1)
    screen.update()
    num += 1
    car_mgmt.drive()
    if num % 6 == 0:
        car_mgmt.create_car()

    for car in car_mgmt.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    if player.ycor() > 280:
        scoreboard.level_up()
        player.level_up()
        car_mgmt.level_up()

screen.exitonclick()
