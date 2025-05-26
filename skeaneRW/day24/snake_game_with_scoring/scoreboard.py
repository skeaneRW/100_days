from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, starting_score):
        super().__init__()
        self.hideturtle()
        self.color('yellow')
        self.pu()
        self.hi_score = self.get_high_score()
        self.goto(110, 280)
        self.point = 0
        self.set_scoreboard(starting_score)

    def set_scoreboard(self, new_score):
        self.pd()
        self.clear()
        self.write(f'score: {new_score}; hi score: {self.hi_score}',font=('Arial',16,'normal'))

    def update_score(self, new_score):
        self.point = new_score
        if new_score > self.hi_score:
           self.update_high_score(new_score)
        self.set_scoreboard(new_score)

    def get_high_score(self):
        with open("skeaneRW/day24/snake_game_with_scoring/hi_score.txt") as file:
            high_score = file.read()
            return int(high_score)
        
    def update_high_score(self, score):
        self.hi_score = score
        with open("skeaneRW/day24/snake_game_with_scoring/hi_score.txt", "w") as file:
            file.write(str(self.hi_score))

    def game_over(self, reason):
        self.clear()
        self.pu()
        self.goto(0,0)
        self.pd()
        self.color('white')
        self.write('game over!', font=('Arial', 24, 'normal'), align='center')
        x,y = self.pos()
        self.goto(x, y-20)
        self.write(f'score: {self.point}; hi score: {self.hi_score}', font=('Arial', 18, 'normal'), align='center')
        self.goto(x, y-40)
        self.write(reason, font=('Arial', 12, 'normal'), align='center')
        self.goto(x,y-60)
        self.write('play again? (y/n)', font=('Arial', 18, 'normal'), align='center')
