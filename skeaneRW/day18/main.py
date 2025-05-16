import turtle as t
from random import randint

class DotPainting:
    def __init__(self, len, wid):
        self.dot_size = 20
        self.gap = 50
        self.grid_height = len
        self.grid_width = wid
        self.starting_x_pos = -300
        self.startiny_y_pos = -300
        self.set_starting_pos()

    def set_starting_pos(self):
        turt.pu()
        turt.speed(0)
        turt.setpos(self.starting_x_pos, self.startiny_y_pos)

    def get_random_color(self):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)
    
    def make_dot(self, color):
        turt.pd()
        turt.color(color)
        turt.fillcolor(color)
        turt.begin_fill()
        turt.circle(20)
        turt.end_fill()
        turt.pu()

    def make_row(self):
        for _ in range(self.grid_width):
            self.make_dot(self.get_random_color())
            turt.forward(self.dot_size + self.gap)


    def set_starting_pos(self):
        turt.pu()
        turt.speed(0)
        turt.setpos(self.starting_x_pos, self.startiny_y_pos)

    def draw(self):
        self.set_starting_pos()
        for i in range(1, self.grid_height + 1):
            self.make_row()
            turt.setpos(self.starting_x_pos, self.startiny_y_pos + (i * (self.dot_size + self.gap)))


turt = t.Turtle()
t.colormode(255)

my_painting = DotPainting(10,10)
my_painting.draw()

screen = t.Screen()
screen.exitonclick()