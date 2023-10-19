import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

contador = 0
level = 1

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_forwards, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    contador += 1

    if (contador == 6):
        car_manager.create_car()
        contador = 0

    car_manager.update_cars()

    #detect collision
    for car in car_manager.cars_list:

        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    #detect finish line
    if player.check_finish_line():
        level += 1
        scoreboard.passed_level()
        car_manager.level += 1
        
        


    screen.update()

screen.exitonclick()