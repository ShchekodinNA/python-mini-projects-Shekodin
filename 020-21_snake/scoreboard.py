from turtle import Turtle
TEXT_COLOR = "white"
ALIGN = "center"
FONT_SIZE = 14
FONT_STILE = "normal"
FONT = "arial"


class ScoreBoard(Turtle):
    def __init__(self, high_score):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.color(TEXT_COLOR)
        self.up()
        self.hideturtle()
        self.goto(0, self.getscreen().window_height()/2 - 20)
        self.upd_scoreboard()


    def upd_scoreboard(self):
        self.write_string(f"Score: {self.score}. High Score: {self.high_score}")

    def add_score(self):
        self.score += 1
        self.upd_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.upd_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write_string(f"Game over. Your score: {self.score}")

    def write_string(self, str):
        self.clear()
        self.write(
            arg=str,
            align=ALIGN,
            font=(FONT, FONT_SIZE, FONT_STILE)
        )
