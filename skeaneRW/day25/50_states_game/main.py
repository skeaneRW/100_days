from turtle import Screen
from state_labeler import StateLabler

class FiftyStates():
    def __init__(self):
        self.screen = Screen()
        self.labeler = StateLabler()
        self.screen_setup()
        self.discovered_states = 0
        self.answers = []
        self.game_is_on = True
        self.get_state()
        self.screen.mainloop()

    def screen_setup(self):
        screen = self.screen
        screen.setup(height=550, width=775)
        screen.bgpic("skeaneRW/day25/50_states_game/blank_states_img.gif")
        screen.title("50 States Quiz")

    def get_state(self):
        while self.game_is_on == True:
            print(self.discovered_states)
            text = self.screen.textinput(f"you named {self.discovered_states} of 50", "name one of the fifty states")
            if text is None:
                self.labeler.get_missed_states(self.answers)
                self.game_is_on = False
            else:
                text = text.title()   
                if self.labeler.check_state(text):
                    self.discovered_states += 1
                    self.answers.append(text)
                if self.discovered_states == 50:
                    self.game_is_on = False

FiftyStates()