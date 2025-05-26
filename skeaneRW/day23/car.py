from turtle import Turtle
from random import randrange, choice as randomchoice

COLORS = ['red', 'orange', 'blue', 'purple']
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, score=0):
        super().__init__()
        self.current_lvl = score
        starting_x = -220 if score > 0 else randrange(-220,220)
        starting_y = randrange(-200,220)
        self.shape("square")
        self.color(randomchoice(COLORS))
        self.pu()
        self.setpos(starting_x, starting_y)
        self.shapesize(stretch_len=2, stretch_wid=1)

    def move(self):
        x,y = self.pos()
        y = randrange(-220, 240) if x < -240 else y
        x = 240 if x < -240 else x
        self.goto(x- (MOVE_DISTANCE + MOVE_INCREMENT * self.current_lvl), y)

    def hits_turtle(self, turtle):
        return self.distance(turtle) < 20
    
    def update_level(self, level):
        self.current_lvl = level