from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# while quiz.still_has_questions():

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)


# while quiz.still_has_questions():  # Esta parte se puede obiar porque ya en la "class" anterior a esto quiz_ui se repite
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
