from turtle import Screen, Turtle


class DashLine(Turtle):
    def __init__(self, color, gap=20, line=20):
        super().__init__()
        self.color(color)
        self.speed(0)
        self.gap = gap
        self.line = line
        self.hideturtle()

    def create_line(self, begin_in, end_in):
        self.up()
        self.goto(begin_in)
        self.setheading(self.towards(end_in))
        while self.distance(end_in) > 5:
            if self.isdown():
                self.up()
                self.forward(self.gap)
            else:
                self.down()
                self.forward(self.line)
        self.up()

