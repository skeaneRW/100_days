#higher lower game
'''
present two options to the player; have them decide which is higher and which is lower.
if they get it right, keep the correctly guessed option and introduce a new option.
if they get it wrong the game is over and they'll be presented with an option to play again.
'''

import random

class Higher_or_Lower:
    def __init__(self):
        self.options = []
        self.score = 0
        self.previous_comparisons = []
        self.option_list = self.get_option_list()
        self.start_game()

    def get_option_list(self):
        return ([
            {"name": "lb of chicken", "cost": 2.99},
            {"name": "salted butter", "cost": 3.96},
            {"name": "lb of ground beef", "cost": 4.49},
            {"name": "chicken thighs", "cost": 1.99},
            {"name": "sour cream", "cost": 1.69},
            {"name": "baby carrots", "cost": 1.59},
            {"name": "celery hearts", "cost": 3.49},
            {"name": "ben and jerrys", "cost": 5.19},
            {"name": "12pk polar seltzer", "cost": 5.00},
            {"name": "12ct free range eggs", "cost": 6.69},
            {"name": "family pack chips ahoy", "cost": 4.19},
            {"name": "Jif peanut butter", "cost": 3.59},
            {"name": "Nutella", "cost": 5.39},
            {"name": "Polaner Jam", "cost": 3.25},
            {"name": "Cheerios", "cost": 5.49},
            {"name": "Pop Tarts", "cost": 2.49},
            {"name": "Red Baron Pizza", "cost": 4.59},
        ])

    def get_option(self):        
        list_of_options = self.option_list
        def fill_options():
            options = self.options
            while True:
                option = random.choice(list_of_options)
                options.insert(0,option)
                if len(self.options) == 2:
                    return options
        options = fill_options()
        #both items cannot be identical:
        while options[0]["name"] == options[1]["name"]: 
            options.pop()
            options = fill_options()
        return options
    
    def compare(self):
        is_higher = self.options[1]["cost"] > self.options[0]["cost"]
        def get_guess():
            while True:
                user_guess = input(f"do you think the prices of {self.options[1]["name"]} is higher or lower than {self.options[0]["name"]}? (h/l)   ").lower()
                if user_guess in ['h','l']:
                    return user_guess
                else:
                    print("please choose either 'h' or 'l'")
        user_guess = get_guess()
        if user_guess == 'h':
            self.score += 1 if is_higher else 0
            return is_higher
        if user_guess == 'l':
            self.score += 1 if not is_higher else 0
            return not is_higher

    def restart(self):
        while True:
            play_again = input("would you like to play again? (y/n) ").lower()
            if play_again == 'y':
                self.options = []
                self.score = 0
                self.previous_comparisons = []
                self.option_list = self.get_option_list()
                self.start_game()
            elif play_again == 'n':
                print("thanks for playing...")
                return
            else:
                print("please choose 'y' or 'n'")


    def start_game(self):
        print("higher or lower: grocery edition!\n")
        print("for each item, you'll tell me whether the price is higher or lower\n keep guessing correctly to get the best score.\n the game ends when you fail to make a correct guess.\n")
        self.options = self.get_option()
        while True:
            round = self.compare()
            if round == True:
                if self.score > 0:
                    print(f"correct! your score is now {self.score}")
                self.option_list.remove(self.options[1])
                self.options.pop()
                self.options = self.get_option()
            else:
                print(f"\nthat's incorrect. game over.\nYour final score is {self.score}")
                return self.restart()

Higher_or_Lower()

