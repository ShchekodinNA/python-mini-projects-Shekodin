from turtle import Turtle

SHAPE = "square"

class Paddle(Turtle):
    def __init__(self, pddl_sgmnt_lngth, is_rght, padding, color="white"):
        super().__init__(shape=SHAPE)
        self.padding = padding
        self.is_rght = is_rght
        self.color(color)
        self.speed(0)
        self.up()
        self.shapesize(stretch_wid=pddl_sgmnt_lngth / 20, stretch_len=1)
        self.pddl_sgmnt_lngth = pddl_sgmnt_lngth
        self.pddl_segments = []
        self.inicialize_paddle()

    def inicialize_paddle(self):
        if self.is_rght:
            self.goto(y=0, x=self.getscreen().window_width() // 2 - self.padding)
        else:
            self.goto(y=0, x=-self.getscreen().window_width() // 2 + self.padding)

    def move_up(self):
        pos = self.pos()
        if pos[1] >= self.getscreen().window_height()/2 - self.pddl_sgmnt_lngth/2 - 20:
            return
        self.goto(x=pos[0], y=pos[1]+20)

    def move_down(self):
        pos = self.pos()
        if pos[1] < -(self.getscreen().window_height()/2 - self.pddl_sgmnt_lngth/2) + 20:
            return
        self.goto(x=pos[0], y=pos[1]-20)
