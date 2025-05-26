from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.v_direction = 10
        self.h_direction = 10
        self.sleep_time = .0865

    def detect_score(self):
        x = self.xcor()
        if x >= 380 or x <= -380:
            self.sleep_time = .0865
            return True
        return False

    def detect_wall(self):
        y = self.ycor()
        if y >= 280:
            self.v_direction = -10
        if y < -280:
            self.v_direction = 10

    def detect_paddle(self, paddles):
        ball_x = self.xcor()
        paddle = paddles[0] if ball_x <= 0 else paddles[1]
        at_goal = ball_x >= 330 if ball_x > 0 else ball_x <= -330
        if self.distance(paddle) < 50 and at_goal:
            if ball_x > 0:
                self.h_direction = -10
            else:
                self.h_direction = 10
            self.sleep_time /= 1.25

    def move(self):
        self.detect_wall()
        x, y = (int(cor) for cor in self.pos())
        new_x = x + self.h_direction
        new_y = y + self.v_direction 
        self.goto(new_x, new_y)
        



