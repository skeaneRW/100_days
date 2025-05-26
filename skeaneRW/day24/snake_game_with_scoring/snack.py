
from turtle import Turtle
from random import randrange

class Snack(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.shapesize(.5,.5,.5)
        self.pu()
        self.setpos(pos)

class Snacks:
    def __init__(self):
        self.snack_count = 6
        self.snacks = self.seed_snacks()

    def seed_snacks(self):
        snacks = []
        while len(snacks) < self.snack_count:
            x = randrange(-280, 280 + 1, 20)
            y = randrange(-280, 280 + 1, 20)
            snack = Snack((x,y))
            snacks.append(snack)
        return snacks