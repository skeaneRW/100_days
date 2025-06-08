import requests
import html
from data import question_data 
from question_model import Question
from quiz_brain import QuizBrain

def get_trivia():
    params ={ "amount": 10,"type": "boolean" }
    TRIVIA_API_URL = "https://opentdb.com/api.php"
    response = requests.get(TRIVIA_API_URL, params=params)
    trivia_list = [{"text":item["question"],"answer":item["correct_answer"]} for item in response.json()["results"]]
    return(trivia_list)

with open("skeaneRW/day34/trivia_revisited/data.py","w") as file:
    file.write(f'question_data = {get_trivia()}')

question_bank = []
for i, data in enumerate(question_data):
    text = html.unescape(data["text"])
    question_bank.append(Question(text, data["answer"]))

quiz = QuizBrain(question_bank)


while not quiz.is_over():
    quiz.next_question()
