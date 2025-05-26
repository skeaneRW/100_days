from turtle import Turtle
import pandas

df = pandas.read_csv("skeaneRW/day25/50_states_game/50_states.csv")

class StateLabler(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()

    def check_state(self, name):
        row = df[df.state == name]
        if len(row):
            x, y = row.x.to_list()[0], row.y.to_list()[0]
            self.place_label(name, (x,y))
            return True
        return False

    def place_label(self, caption, pos):
        self.goto(pos)
        self.pd()
        self.write(caption, align="center", font=("Arial", 10, "normal"))
        self.pu()

    def get_missed_states(self, answers):
        all_states = df.state
        missing_states = {
            "state": [],
            "x": [],
            "y": [],
        }
        for state in all_states:
            if state not in answers:
                missing_states["state"].append(state)
                x = int(df[df.state == state].iloc[0].x)
                y = int(df[df.state == state].iloc[0].y)
                missing_states["x"].append(x)
                missing_states["y"].append(y)
        new_df = pandas.DataFrame(missing_states)
        new_df.to_csv("skeaneRW/day25/50_states_game/missing_states.csv")

