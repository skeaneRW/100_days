from turtle import Turtle, Screen
from random import randrange
from time import sleep

class SnakePart(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.pu()
        self.setpos(pos)

class Snake:
    def __init__(self, pos_list):
        self.snake = self.seed_snake(pos_list)
        
    def seed_snake(self, positions):
        snake_parts = []
        for position in positions:
            snake_part = SnakePart(position)
            snake_parts.append(snake_part)
        return snake_parts
    
    def move_head(self, head, dir):
        if dir == 'Left':
            head.setheading(180)
        if dir == 'Right':
            head.setheading(0)
        if dir == 'Up':
            head.setheading(90)
        if dir == 'Down':
            head.setheading(270)
        head.forward(20)

    def grow(self, dir):
        head_pos = self.snake[0].pos()
        self.snake.insert(1,SnakePart(head_pos))
        self.move_head(self.snake[0],dir)

    def move(self, dir):
        for segment in range(len(self.snake)-1, 0, -1):
            next_pos = self.snake[segment-1].pos()
            self.snake[segment].setpos(next_pos)
        self.move_head(head=self.snake[0], dir=dir)

    def get_positions(self):
        positions = []
        for segment in self.snake:
            positions.append(segment.pos())
        return positions

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

class Scoreboard:
    def __init__(self, starting_score):
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.color('yellow')
        self.pen.pu()
        self.pen.goto(210, 280)
        self.point = 0
        self.set_scoreboard(starting_score)

    def set_scoreboard(self, new_score):
        self.pen.pd()
        self.pen.clear()
        self.pen.write(f"score: {new_score}",font=('Arial',16,'normal'))

    def update_score(self, new_score):
        self.point = new_score
        self.set_scoreboard(new_score)

class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.snake = Snake([(0,0),(20,0),(40,0)])
        self.snacks = Snacks()
        self.point = 0
        self.score = Scoreboard(0)
        self.speed = .45
        self.set_screen()

    def detect_snack(self, dir):
        head_x, head_y = self.snake.snake[0].pos()
        head_x, head_y = int(head_x), int(head_y)
        for ea_snack in self.snacks.snacks:
            snack_x, snack_y = ea_snack.pos()
            snack_x, snack_y = int(snack_x), int(snack_y)
            if (head_x + 10 > snack_x > head_x - 10) and (head_y + 10 > snack_y > head_y - 10):
                random_x, random_y = randrange(-280, 280 + 1, 20), randrange(-280, 280 + 1, 20)
                ea_snack.goto(random_x,random_y)
                self.snake.grow(dir)
                self.point += 1
                self.score.update_score(self.point)
                self.speed *= .85
        
    def set_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.screen.bgcolor('black')
        self.screen.title('python snake game')
        self.screen.listen()
        self.screen.onkey(fun=lambda: self.move("Left"), key="Left")
        self.screen.onkey(fun=lambda: self.move("Right"), key="Right")
        self.screen.onkey(fun=lambda: self.move("Up"), key="Up")
        self.screen.onkey(fun=lambda: self.move("Down"), key="Down")
        self.screen.exitonclick()

    def game_over(self):
        def out_of_bounds():
            x_limit, y_limit = (305, 305)
            for position in self.snake.get_positions():
                x, y = position
                in_horizontal = -x_limit < x < x_limit
                in_vertical = -y_limit < y < y_limit
                if (not in_horizontal or not in_vertical):
                    return True
            return False
        
        def snake_bit_itself():
            snake_head_x, snake_head_y = self.snake.snake[0].pos()
            snake_head_x, snake_head_y = int(snake_head_x), int(snake_head_y)
            snake_tail = self.snake.snake[1::]
            if len(snake_tail) >= 3: # to avoid bites at the beginning of play.
                for segment in snake_tail:
                    segment_x, segment_y = segment.pos()
                    segment_x, segment_y = int(segment_x), int(segment_y)
                    if (segment_x + 10 > snake_head_x > segment_x - 10) and (segment_y + 10 > snake_head_y > segment_y - 10):
                        return True

        reason = 'your snake hit the wall!' if out_of_bounds() else 'your snake bit itself!'        
        if out_of_bounds() or snake_bit_itself():
            self.show_game_over(reason)
            return True
        else:
            return False
    
    def show_game_over(self, reason):
        self.screen.reset()
        caption = Turtle()
        caption.color('white')
        caption.write('game over!', font=('Arial', 24, 'normal'), align='center')
        x,y = caption.pos()
        caption.goto(x, y-20)
        caption.write(f'score: {self.point}', font=('Arial', 18, 'normal'), align='center')
        caption.goto(x, y-40)
        caption.write(reason, font=('Arial', 12, 'normal'), align='center')
        

    def move(self, dir):
        while not self.game_over():
            self.snake.move(dir)
            sleep(self.speed)
            self.detect_snack(dir)
            self.screen.update()

SnakeGame()