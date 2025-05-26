from turtle import Screen
from time import sleep
from player import Player
from scoreboard import Scoreboard
from car import Car

class TurtleCrossing:
    def __init__(self):
        self.game_on = True
        self.screen = Screen()
        self.player = Player()
        self.score = Scoreboard()
        self.cars = []
        self.num_cars = 6
        self.setup_screen()
        self.play_game()

    def setup_screen(self):
        screen = self.screen
        screen.setup(width=500, height=600)
        screen.listen()
        screen.tracer(0)
        screen.onkey(fun=self.player.go_up, key="Up")
        screen.onkey(fun=self.player.go_down, key="Down")
        screen.onkey(fun=self.player.go_left, key="Left")
        screen.onkey(fun=self.player.go_right, key="Right")
        screen.onscreenclick(self.quit)

    def play_game(self):
        while self.game_on:
            if len(self.cars) < self.num_cars:
                self.cars.append(Car(self.score.current_score()))
            if self.player.at_goal():
                self.score.increment()
                self.score.update()
                self.num_cars += 1
                for car in self.cars:
                    car.update_level(self.score.score)
            for car in self.cars:
                car.move()
                if car.hits_turtle(self.player):
                    self.game_over()
            self.screen.update()
            sleep(.5)

    def game_over(self):
        self.game_on = False
        self.score.show_game_over()
        self.screen.update()
        self.screen.exitonclick()

    def quit(self, x, y):
        self.game_on = False
        self.screen.bye()

        
TurtleCrossing()