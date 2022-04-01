from turtle import Turtle


HEADING = 90
COLOR = "RED"
MOVE_DISTANCE = 10
SHAPE = "turtle"


class Player(Turtle):
    def __init__(self, starting_y=int):
        super().__init__(shape=SHAPE)
        self.color(COLOR)
        self.starting_y = starting_y
        self.up()
        self.speed(0)
        self.reinitialize()

    def forward_moving(self):
        self.forward(MOVE_DISTANCE)

    def reinitialize(self):
        self.setheading(HEADING)
        self.goto((0, self.starting_y))