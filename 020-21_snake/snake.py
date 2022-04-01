from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = "square"
HEAD_COLOR = "red"


class Snake:
    def __init__(self, segments_num):
        self.start_segments = segments_num
        self.segments_num = segments_num
        self.snake_segments = []
        self.snake_head = Turtle()
        self.reset_snake()

    def create_snake(self):
        for i in range(self.segments_num):
            nw_trtl = self.create_new_segment((-i * 20, 0))
            self.snake_segments.append(nw_trtl)

    @staticmethod
    def create_new_segment(position):
        nw_trtl = Turtle(shape=SHAPE)
        nw_trtl.up()
        nw_trtl.goto(position)
        nw_trtl.color((255, 255, 255))
        return nw_trtl

    def forward(self):
        for trtl in self.snake_segments:
            trtl.forward(20)
        heading = self.snake_head.heading()
        for i in range(1, len(self.snake_segments)):
            heading_next = self.snake_segments[i].heading()
            heading_next, heading = heading, heading_next
            self.snake_segments[i].setheading(heading_next)

    def trn_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def trn_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def trn_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def trn_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def extend(self):
        new_seg = self.create_new_segment(self.snake_segments[-1].pos())
        new_seg.backward(20)
        self.snake_segments.append(new_seg)

    def reset_snake(self):
        for segment in self.snake_segments:
            segment.goto(x=10000, y=10000)
        self.snake_segments.clear()
        self.segments_num = self.start_segments
        self.create_snake()
        self.snake_head = self.snake_segments[0]
        self.snake_head.color(HEAD_COLOR)
