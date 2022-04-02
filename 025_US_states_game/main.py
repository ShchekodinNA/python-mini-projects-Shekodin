import pandas
from turtle import Turtle, Screen
from text_writer import TextWriter


data = pandas.read_csv("50_states.csv")
screen = Screen()
screen.bgpic("blank_states_img.gif")
writer = TextWriter()
score = 0
question_number = data.state.count()

while score <= question_number:
    screen.title(f"U.S. State guess game | SCORE = {score}/{question_number}")
    user_answer = screen.textinput(title="Guess the State", prompt="Enter State name (or 'exit' to leave the game):")
    if user_answer == "exit":
        writer.color("red")
        break
    user_answer = user_answer.title()
    current_state = data[data.state == user_answer].to_list()#values.tolist()
    if len(current_state) > 0:
        writer.write_str_on_pos(x=current_state[0][1], y=current_state[0][2], text=current_state[0][0])
        score += 1
        data = data.drop(data[data.state == user_answer].index)
else:
    writer.color("green")

writer.font_size = 20
writer.write_str_on_pos(x=0, y=0, text=f"Your SCORE = {score}/{question_number}")
screen.exitonclick()

data.to_csv("missed_states.csv")
