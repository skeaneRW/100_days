from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.pu()
        self.goto(0, -260)
        self.setheading(90)

    def go_up(self):
        self.setheading(90)
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.setheading(270)
        if self.ycor() > -260:
            self.goto(self.xcor(), self.ycor() - 20)

    def go_left(self):
        self.setheading(180)
        if self.xcor() > -220: 
            self.goto(self.xcor() - 20, self.ycor())

    def go_right(self):
        self.setheading(0)
        if self.xcor() < 220:           
            self.goto(self.xcor() + 20, self.ycor())

    def at_goal(self):
        if self.ycor() > 300:
            self.goto(0,-260)
            return True
        return False