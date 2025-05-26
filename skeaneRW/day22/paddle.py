from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, initial_position):
        super().__init__() 
        self.pu()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(initial_position)

    def move_paddle(self, dir):
        move_increment = 10 if dir == 'Up' else -10
        x, y = self.pos()    
        self.goto(x, y + move_increment)
        