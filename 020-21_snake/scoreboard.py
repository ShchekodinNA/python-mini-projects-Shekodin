from turtle import Turtle
TEXT_COLOR = "white"
ALIGN = "center"
FONT_SIZE = 14
FONT_STILE = "normal"
FONT = "arial"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(TEXT_COLOR)
        self.up()
        self.hideturtle()
        self.goto(0, self.getscreen().window_height()/2 - 20)
        self.write_string(f"SCORE: {self.score}")

    def add_score(self):
        self.score += 1
        self.write_string(f"SCORE: {self.score}")

    def game_over(self):
        self.goto(0, 0)
        self.write_string(f"Game over. Your score: {self.score}")

    def write_string(self, str):
        self.clear()
        self.write(
            arg=str,
            align=ALIGN,
            font=(FONT, FONT_SIZE, FONT_STILE)
        )
