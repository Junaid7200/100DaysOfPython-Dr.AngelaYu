from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_uni = ui.QuizInterface(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# HTML entities are interfering and making the text being printed weird


# # concrete datatypes in python
# age:int
# name:str
# # could do same with function parameters
# def func (age:int) -> bool: #returns bool and accepts parameters of int type
#     return age > 18