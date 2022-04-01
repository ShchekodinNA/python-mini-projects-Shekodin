from turtle import Turtle
import random
SHAPE = "circle"
COLOR = "white"
STEP = 3


class Ball(Turtle):
    def __init__(self, is_bounce=False):
        super().__init__(shape=SHAPE)
        self.color(COLOR)
        self.up()
        self.is_bounce = is_bounce
        self.setheading(random.randint(0, 359))
        self.upper_line = self.getscreen().window_height()//2 - 10
        self.lower_line = -self.getscreen().window_height()//2 + 20

    def move_forward(self):
        if self.is_bounce:
            self.bounce_y()
        self.forward(STEP)

    def bounce_y(self):
        if self.pos()[1] > self.upper_line or self.pos()[1] < self.lower_line:
            self.setheading(-self.heading())

    def bounce_x(self):
        self.setheading(-self.heading())
        self.left(180)

    def reinicialize(self):
        self.goto(0, 0)
        self.setheading(random.randint(0, 359))