from turtle import Turtle


class TextWriter(Turtle):
    def __init__(self, font="arial", font_size=10, font_stile="normal", align="center"):
        super().__init__()
        self.font = font
        self.align = align
        self.font_stile = font_stile
        self.font_size = font_size
        self.up()
        self.hideturtle()
        self.speed(0)

    def write_str_on_pos(self, x, y, text):
        self.goto((x, y))
        self.write(
            arg=text,
            align=self.align,
            font=(self.font, self.font_size, self.font_stile)
        )
