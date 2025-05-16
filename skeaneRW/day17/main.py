from data import question_data 
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i, data in enumerate(question_data):
    question_bank.append(Question(data["text"], data["answer"]))

quiz = QuizBrain(question_bank)

while not quiz.is_over():
    quiz.next_question()
