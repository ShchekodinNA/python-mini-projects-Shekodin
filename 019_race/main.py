import random
from turtle import Turtle, Screen


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
WIDTH = 500
HEIGHT = 400


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
us_bet = screen.textinput(prompt="Which color win?", title="Set bet")
for i in range(len(colors)):
    new_trtl = Turtle()
    new_trtl.color(colors[i])
    new_trtl.shapesize(2)
    new_trtl.up()
    new_trtl.goto(x=- WIDTH / 2 + 10, y=-90 + 30 * i)

is_race_on = True


while is_race_on:
    for trtl in screen.turtles():
        trtl.forward(random.randint(0, 10))
        if trtl.pos()[0] >= WIDTH/2:
            is_race_on = False
            win_color = trtl.pencolor()
            print(win_color)

if us_bet == win_color:
    print(f"You Win! Congrats.")
else:
    print(f"You Lose! {win_color} arrow won the race")
screen.exitonclick()



