from turtle import Screen
from random import randrange
from snake import Snake
from snack import Snacks
from scoreboard import Scoreboard
from time import sleep

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
        self.screen.onkey(fun=self.reset_game, key="y")
        self.screen.onkey(fun=self.quit, key="n")
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
        self.score.game_over(reason)

    def move(self, dir):
        while not self.game_over():
            self.snake.move(dir)
            sleep(self.speed)
            self.detect_snack(dir)
            self.screen.update()

    def reset_game(self):
        self.screen.reset()
        self.screen = Screen()
        self.snake = Snake([(0,0),(20,0),(40,0)])
        self.snacks = Snacks()
        self.point = 0
        self.score = Scoreboard(0)
        self.speed = .45
        self.set_screen()
    
    def quit(self):
        self.screen.bye()

SnakeGame()