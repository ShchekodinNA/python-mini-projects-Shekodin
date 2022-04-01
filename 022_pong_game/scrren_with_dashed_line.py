from turtle import Screen, Turtle


class DashLine(Turtle):
    def __init__(self, begin_in, end_in, color, gap=20, line=20):
        super().__init__()
        self.end_in = end_in
        self.color(color)
        self.gap = gap
        self.line = line
        self.hideturtle()
        self.up()
        self.goto(begin_in)
        self.setheading(self.towards(end_in))
        self.create_line()

    def create_line(self):
        while self.distance(self.end_in) > 5:
            if self.isdown():
                self.up()
                self.forward(self.gap)
            else:
                self.down()
                self.forward(self.line)
