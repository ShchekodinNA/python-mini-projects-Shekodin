from turtle import Turtle
TEXT_COLOR = "white"
ALIGN = "center"
FONT_SIZE = 40
FONT_STILE = "normal"
FONT = "arial"


class ScoreTable(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color(TEXT_COLOR)
        self.up()
        self.hideturtle()
        self.goto(0, self.getscreen().window_height()/2 - 60)
        self.write_string(f"{self.l_score}          {self.r_score}")

    def add_score(self, is_right):
        if is_right:
            self.r_score += 1
        else:
            self.l_score += 1
        self.write_string(f"{self.l_score}          {self.r_score}")

    def game_over(self):
        self.goto(0, 0)
        self.write_string(f"{self.l_score}          {self.r_score}")

    def write_string(self, str):
        self.clear()
        self.write(
            arg=str,
            align=ALIGN,
            font=(FONT, FONT_SIZE, FONT_STILE)
        )
