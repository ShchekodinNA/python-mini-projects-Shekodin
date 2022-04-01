class QuizBran:
    def __init__(self, qst_list):
        self.qst_number = 0
        self.qst_list = qst_list
        self.score = 0

    def ask(self):
        current_question = self.qst_list[self.qst_number]
        self.qst_number += 1
        user_answer = input(f"Q.{self.qst_number}: {current_question.question}\n"
                            "Is that right? (True,False): ")
        self.check_answer(user_answer, current_question.answer)

    def have_next_question(self):
        return len(self.qst_list) > self.qst_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You right!")
            self.score += 1
        else:
            print(f"You wrong! Correct answer was '{correct_answer}'")
        print(f"score: {self.result()}")

    def result(self):
        return f"{self.score}/{self.qst_number}"
