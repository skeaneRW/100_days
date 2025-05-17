import random

class HigherLower:
    def __init__(self):
        self.options = []
        self.score = 0
        self.previous_comparisons = []
        self.option_list = self.get_option_list()

    def get_option_list(self):
        return [
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
        ]

    def get_option(self):
        options = random.sample(self.option_list, 2)
        self.options = options
        return options

    def compare(self):
        is_higher = self.options[1]["cost"] > self.options[0]["cost"]
        while True:
            user_guess = input(
                f"Do you think the price of {self.options[1]['name']} is higher or lower than {self.options[0]['name']}? (h/l): "
            ).lower()
            if user_guess in ['h', 'l']:
                break
            print("Please choose either 'h' or 'l'")
        if user_guess == 'h':
            if is_higher:
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
            return is_higher
        else:
            if not is_higher:
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect!")
            return not is_higher

    def start_game(self):
        print("Welcome to the Higher or Lower game!")
        print("You will be given two items and you have to guess which one is more expensive.")
        print("Type 'h' for higher and 'l' for lower.")
        print("Let's start!")
        self.score = 0
        while True:
            self.get_option()
            correct = self.compare()
            print(f"Your current score is: {self.score}")
            if not correct:
                play_again = input("Incorrect! Do you want to play again? (y/n): ").lower()
                if play_again != 'y':
                    break
                self.score = 0  # Optionally reset score on new game
        print(f"Thanks for playing! Your final score is: {self.score}")

if __name__ == "__main__":
    game = HigherLower()
    game.start_game()