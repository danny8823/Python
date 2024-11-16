import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('FROGGER but with a turtle')
screen.tracer(0)
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")
score_board = Scoreboard()
game_is_on = True

while game_is_on:
    score_board
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        score_board.up_level()
        player.go_to_start()

screen.exitonclick()
