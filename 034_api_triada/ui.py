from tkinter import *
from quiz_brain import QuizBrain
FONT = 'Tahoma'
FONT_SIZE = 25
THEME_COLOR = "#375362"


class UI:
    def __init__(self, quiz_brain: QuizBrain, title='Quizbrain'):
        self.qz_brain_inst = quiz_brain
        self.window = Tk()
        self.window.title(title)
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=25, pady=25)
        self.score = Label(text=f"Score: 0", font=(FONT, FONT_SIZE), bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        yes_img = PhotoImage(file="images/true.png")
        no_img = PhotoImage(file="images/false.png")

        self.btn_yes = Button(image=yes_img, highlightthickness=0, command=self.press_yes, justify="left")
        self.btn_yes.grid(column=0, row=2)

        self.btn_no = Button(image=no_img, highlightthickness=0, command=self.press_no)
        self.btn_no.grid(column=1, row=2)

        self.question = Label(width=20, wraplength=300, height=15, font=(FONT, FONT_SIZE))
        self.question.grid(column=0, columnspan=2, row=1, pady=30)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        q_text = self.qz_brain_inst.next_question()
        self.question.config(text=q_text)

    def press_yes(self):
        self.give_feedback(self.qz_brain_inst.check_answer("True"))

    def press_no(self):
        self.give_feedback(self.qz_brain_inst.check_answer("False"))

    def give_feedback(self, is_right):
        self.btn_yes.config(state="disabled")
        self.btn_no.config(state="disabled")
        if is_right:
            self.question.config(bg="green")
            self.qz_brain_inst.score += 1
        else:
            self.question.config(bg="red")
        self.score.config(text=f"Score: {self.qz_brain_inst.score}")
        self.window.after(1000, self.get_new_question)

    def get_new_question(self):
        self.question.config(bg="white")
        if self.qz_brain_inst.still_has_questions():
            self.get_question()
            self.btn_yes.config(state="normal")
            self.btn_no.config(state="normal")
        else:
            self.question.config(text="Game Over!")

        self.score.config(text=f"Score: {self.qz_brain_inst.score}")