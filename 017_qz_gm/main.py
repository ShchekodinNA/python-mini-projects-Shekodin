from data import question_data, new_data
import quiz_brain
import question_model

question_bank = []

for line in question_data:
    question_bank.append(
        question_model.Question(
            question=line["text"], answer=line["answer"]
        )
    )
new_question_bank = []
for line in new_data:
    new_question_bank.append(
        question_model.Question(question=line["question"], answer=line["correct_answer"])
    )
lo_quiz_brain = quiz_brain.QuizBran(new_question_bank)

while lo_quiz_brain.have_next_question():
    lo_quiz_brain.ask()

print(f"You completed quiz.\nYour final score is {lo_quiz_brain.result()}")