from turtle import Turtle
import random
SHAPE = "turtle"
COLOR = "green"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.width = self.getscreen().window_width()
        self.height = self.getscreen().window_height()
        self.shape(SHAPE)
        self.color(COLOR)
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        self.random_generate_position()

    def random_generate_position(self):
        self.goto(
            x=random.randint(-(self.width // 2 - 20), self.width // 2 - 20),
            y=random.randint(-(self.height // 2 - 20), self.width // 2 - 20)
        )
