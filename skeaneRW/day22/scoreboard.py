from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = {"left_player": 0, "right_player": 0}
        self.color("white")
        self.shape("square")
        self.pu()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score["left_player"], align="center",font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score["right_player"], align="center",font=("Courier", 80, "normal"))

    def add_point(self, player):
        if player == 'left':
            self.score["left_player"] += 1
        if player == 'right':
            self.score["right_player"] += 1
        self.update_score()

