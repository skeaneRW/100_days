import requests

class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = self.get_question_bank()

    def reset_questions(self):
        self.question_number = 0
        self.question_list = self.get_question_bank()
        self.current_question = self.question_list[self.question_number]

    def get_question_bank(self):
        params ={ "amount": 10,"type": "boolean" }
        TRIVIA_API_URL = "https://opentdb.com/api.php"
        response = requests.get(TRIVIA_API_URL, params=params)
        trivia_list = [{"text":item["question"],"answer":item["correct_answer"]} for item in response.json()["results"]]
        self.current_question = trivia_list[0]
        return(trivia_list)

    def next_question(self):
        self.question_number += 1    
        try:
            self.current_question = self.question_list[self.question_number]
        except(IndexError):
            return self.reset_questions()

    def check_user_response(self, user_response: str, correct_answer: str) -> bool:
        if user_response == correct_answer:
            self.score += 1  
            return True
        else:
            return False

    def is_over(self):
        return len(self.question_list) <= self.question_number


