class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        current_question =  self.question_list[self.question_number]
        self.question_number += 1
        user_response = input(f"Q{self.question_number}: {current_question.text} (True/False)?  ").title()
        self.check_user_response(user_response, current_question.answer)

    def check_user_response(self, user_response, correct_answer):
        if user_response == correct_answer:
            self.score += 1
            return print(f"that's correct. Your current score is {self.score}/{len(self.question_list)}\n")
        else:
            return print(f"that's wrong. Your current score is {self.score}/{len(self.question_list)}\n")

    def is_over(self):
        return len(self.question_list) == self.question_number


