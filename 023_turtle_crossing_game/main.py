import time
from scrren_with_dashed_line import DashLine
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


BG_COLOR = (0, 0, 0)
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
BEGIN_CAR_AMOUNT = 10
CAR_PER_LVL = 2
DASH_LINE_COLOR = "white"


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.bgcolor(BG_COLOR)
start_point = -SCREEN_HEIGHT//2 + 20
end_point = SCREEN_HEIGHT//2 - 20
player = Player(starting_y=start_point)


scoreboard = ScoreBoard()


dash_line = DashLine(color=DASH_LINE_COLOR, gap=5, line=3)
list_of_y = []
for i in range(start_point + 45, end_point -14, 30):
    list_of_y.append(i)
for i in range(start_point + 30, end_point -29, 30):
    dash_line.create_line(begin_in=(SCREEN_WIDTH//2, i), end_in=(-SCREEN_WIDTH//2, i))

car_manager = CarManager(list_of_start_y=list_of_y, num_of_cars=BEGIN_CAR_AMOUNT, collision_object=player)
car_manager.create_car()

screen.listen()
screen.onkeypress(player.forward_moving, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move_all_cars()
    if player.pos()[1] >= end_point:
        player.reinitialize()
        car_manager.starting_car_speed += 1
        car_manager.randomize_all_car_pos()
        scoreboard.add_score()
        for _ in range(CAR_PER_LVL):
            car_manager.create_car()
    screen.update()
    if car_manager.is_have_collision():
        scoreboard.game_over()
        break

screen.exitonclick()
