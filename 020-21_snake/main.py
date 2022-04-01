from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
WIDTH = 600
HEIGHT = 600
BEGINNING_LENGTH = 3
TIME_PER_STEP = 100
scrn = Screen()


def clear_score():
    if scrn.textinput(title="Clear high score", prompt="Type \"clear\" if you want reset high score:") == "clear":
        with open("high_score.txt", mode="w") as hgh_txt_inner:
            hgh_txt_inner.write("0")
        scoreboard.high_score = 0
        scoreboard.upd_scoreboard()
    scrn.listen()


def write_new_high_score():
    scoreboard.reset()
    with open("high_score.txt", mode="w") as hgh_txt:
        hgh_txt.write(str(scoreboard.high_score))
    snake.reset_snake()


def exit_game():
    global is_continue
    write_new_high_score()
    is_continue = False


scrn.setup(width=WIDTH, height=HEIGHT)
scrn.bgcolor((0, 0, 0))
scrn.title("Snake Nikita's Schekodin project")
scrn.colormode(255)
scrn.tracer(0)

snake = Snake(segments_num=BEGINNING_LENGTH)
food = Food()
with open("high_score.txt") as hgh_txt:
    scoreboard = ScoreBoard(high_score=int(hgh_txt.read()))

scrn.listen()
scrn.onkey(snake.trn_up, "Up")
scrn.onkey(snake.trn_left, "Left")
scrn.onkey(snake.trn_right, "Right")
scrn.onkey(snake.trn_down, "Down")
scrn.onkey(clear_score, "c")
scrn.onkey(exit_game, "q")

is_continue = True
while is_continue:
    if snake.snake_head.pos()[0] > WIDTH/2 - 20\
            or snake.snake_head.pos()[0] < - WIDTH/2 + 20\
            or snake.snake_head.pos()[1] > + HEIGHT/2 - 20\
            or snake.snake_head.pos()[1] < - HEIGHT/2 + 20:
        write_new_high_score()
    if snake.snake_head.distance(food) < 16:
        food.random_generate_position()
        scoreboard.add_score()
        snake.extend()
    snake.forward()
    for seg in snake.snake_segments[1:]:
        if snake.snake_head.distance(seg) < 18:
            write_new_high_score()
    scrn.update()
    time.sleep(TIME_PER_STEP*0.001)


