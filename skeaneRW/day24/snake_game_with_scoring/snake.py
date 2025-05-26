from turtle import Turtle

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