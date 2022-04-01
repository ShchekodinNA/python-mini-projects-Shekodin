from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
WIDTH = 600
HEIGHT = 600
BEGINNING_LENGTH = 3
TIME_PER_STEP = 200
scrn = Screen()

scrn.setup(width=WIDTH, height=HEIGHT)
scrn.bgcolor((0, 0, 0))
scrn.title("Snake Nikita's Schekodin project")
scrn.colormode(255)
scrn.tracer(0)

snake = Snake(segments_num=BEGINNING_LENGTH)
snake_head = snake.snake_head
food = Food()
scoreboard = ScoreBoard()


scrn.listen()
scrn.onkey(snake.trn_up, "Up")
scrn.onkey(snake.trn_left, "Left")
scrn.onkey(snake.trn_right, "Right")
scrn.onkey(snake.trn_down, "Down")
is_continue = True
while is_continue:
    if snake_head.pos()[0] > WIDTH/2 - 20\
            or snake_head.pos()[0] < - WIDTH/2 + 20\
            or snake_head.pos()[1] > + HEIGHT/2 - 20\
            or snake_head.pos()[1] < - HEIGHT/2 + 20:
        scoreboard.game_over()
        break
    if snake_head.distance(food) < 16:
        food.random_generate_position()
        scoreboard.add_score()
        snake.extend()

    snake.forward()
    for seg in snake.snake_segments[1:]:
        if snake_head.distance(seg) < 18:
            is_continue = False
    scrn.update()
    time.sleep(TIME_PER_STEP*0.001)
scoreboard.game_over()
scrn.exitonclick()
