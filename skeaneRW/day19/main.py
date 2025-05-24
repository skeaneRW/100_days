from turtle import Turtle, Screen
from random import randint


class Racer:
    def __init__(self, color, starting_pos):
        self.turtle = Turtle()
        self.turtle.shape('turtle')
        self.turtle.color(color)
        self.place_turtle(starting_pos)
        self.turtle.pu()

    def place_turtle(self, starting_pos):
        self.turtle.pu()
        self.turtle.setpos(starting_pos)
        self.turtle.pd()

    def set_speed(self):
        return randint(5,10)
    
    def fwd(self):
        speed = self.set_speed()
        self.turtle.forward(speed)

    def get_winner(self):
        x, _ = self.turtle.pos()
        if x > 400: 
            print(self.turtle.color()[0])
            return self.turtle.color()[0]

class Game:
    def __init__(self, racers):
        self.screen = Screen()
        self.racers = racers
        self.pen = Turtle()
        self.pen.pu()
        self.pen.hideturtle()
        self.winner = None
        self.set_turtle_labels()
        self.screen.listen()
        self.screen.onkey(key="space", fun=self.move_turtle)
        self.screen.exitonclick()

    def set_instructions(self):
        self.pen.setpos(0, -100)
        self.pen.write("press spacebar to begin", align='center', font=('Arial', 16, 'normal'))

    def set_turtle_labels(self):
        for ea in self.racers:
            x, y = ea.turtle.pos()
            self.pen.setpos(x + 20, y-5)
            self.pen.write(ea.turtle.color()[0], align='left', font=('Arial', 16, 'normal'))
        self.player_guess = self.get_player_guess()
        return

    def get_player_guess(self):
        guess = self.screen.textinput("pick a winner", "who will win?")
        self.set_instructions()
        return guess

    def move_turtle(self):
        self.pen.clear()
        while not self.winner:
            for turtle in self.racers:
                if not turtle.get_winner():
                    turtle.fwd()
                else:
                    self.winner = turtle.get_winner()
                    self.check_winner()
                    return 
                
    def check_winner(self):
        self.pen.setpos(0,0)
        if self.player_guess.lower() == self.winner:
            self.pen.write(f"{self.winner} is the winner. you win!", align='center', font=('Arial', 16, 'normal'))
        else:
            self.pen.write(f"{self.winner} is the winner. you lose", align='center', font=('Arial', 16, 'normal'))
            

def create_racers():
    colors = ['red', 'orange', 'blue', 'indigo', 'violet']
    starting_x = -400
    starting_y = 40
    racers = []        
    for i in range(len(colors)):
        racers.append(Racer(colors[i], (starting_x, starting_y * i - starting_y )))
    return racers

racers = create_racers()
Game(racers)
