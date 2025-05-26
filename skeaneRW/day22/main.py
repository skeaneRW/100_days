from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

class Pong:
    def __init__(self):
        self.game_is_on = True
        self.screen = Screen()
        self.set_screen()
        self.left_paddle = Paddle((-350,0))
        self.right_paddle = Paddle((350,0))
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.run_game()

    def set_screen(self):      
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.screen.title('pong')
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkey(fun=lambda: self.right_paddle.move_paddle('Up'), key='Up')
        self.screen.onkey(fun=lambda: self.right_paddle.move_paddle('Down'), key='Down')
        self.screen.onkey(fun=lambda: self.left_paddle.move_paddle('Up'), key='w')
        self.screen.onkey(fun=lambda: self.left_paddle.move_paddle('Down'), key='s')
        self.screen.onscreenclick(self.quit)
        self.screen.onkey(fun=self.quit, key='q')
 
    def run_game(self):
        while self.game_is_on:
            time.sleep(self.ball.sleep_time)
            self.screen.update()
            self.ball.move()
            self.ball.detect_paddle(paddles=[self.left_paddle, self.right_paddle])
            if self.ball.detect_score():
                point_winner = 'left' if self.ball.xcor() else 'right'
                self.scoreboard.add_point(point_winner)
                self.ball.h_direction *= -1
                self.ball.goto(0,0) 

    def quit(self, x, y):
        self.game_is_on = False


Pong()
    

