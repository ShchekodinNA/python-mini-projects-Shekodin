from scoretable import ScoreTable
from scrren_with_dashed_line import DashLine
from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
STANDARD_TIME = 0.006
WIDTH = 1000
HEIGHT = 600
BEGINNING_LENGTH = 3
TIME_PER_STEP = 200
PADDLE_LENGTH = 100
PADDING = 20
PER_GOAL_TIME_SPEEDING = 0.9


def left_game():
    global is_on
    is_on = False


time_per_step = STANDARD_TIME
half_height = HEIGHT // 2
half_width = WIDTH // 2
scrn = Screen()
scrn.setup(width=WIDTH, height=HEIGHT)
scrn.bgcolor((0, 0, 0))
scrn.title("Pong Nikita's Schekodin project")
scrn.colormode(255)
scrn.tracer(0)
ball = Ball(is_bounce=True)
DashLine(begin_in=(0, half_height), end_in=(0, -half_height), color="white")
left_paddle = Paddle(pddl_sgmnt_lngth=PADDLE_LENGTH, padding=PADDING, is_rght=False)
right_paddle = Paddle(pddl_sgmnt_lngth=PADDLE_LENGTH, padding=PADDING, is_rght=True)
scrn.update()
scoretable = ScoreTable()
scrn.listen()
scrn.onkeypress(left_paddle.move_up, "4")
scrn.onkeypress(left_paddle.move_down, "1")
scrn.onkeypress(right_paddle.move_up, "6")
scrn.onkeypress(right_paddle.move_down, "3")
scrn.onkeypress(left_game, "5")
time.sleep(1)
is_on = True
while is_on:
    scrn.update()

    if (ball.distance(left_paddle) <= PADDLE_LENGTH // 2 and ball.pos()[0] < left_paddle.pos()[0] + 20) \
            or (ball.distance(right_paddle) <= PADDLE_LENGTH // 2 and ball.pos()[0] > right_paddle.pos()[0] - 20):
        ball.bounce_x()
        time_per_step *= PER_GOAL_TIME_SPEEDING
    if ball.pos()[0] < -half_width:
        ball.reinicialize()
        time_per_step = STANDARD_TIME
        scoretable.add_score(is_right=True)
        scrn.update()
        time.sleep(0.5)
    if ball.pos()[0] > half_width:
        ball.reinicialize()
        time_per_step = STANDARD_TIME
        scoretable.add_score(is_right=False)
        scrn.update()
        time.sleep(0.5)
    ball.move_forward()
    time.sleep(time_per_step)

scoretable.game_over()
time.sleep(2)

# scrn.exitonclick()
