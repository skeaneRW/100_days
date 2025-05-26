from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pu()
        self.update()

    def update(self):
        self.clear()
        self.goto(-220, 260)
        self.write((f"score: {self.score}"), font=('Arial', 14, "normal"))

    def increment(self):
        self.score += 1
    def current_score(self):
        return self.score

    def show_game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.color('red')
        self.write((f"game over!"),align="center",font=('Arial', 14, "bold"))
