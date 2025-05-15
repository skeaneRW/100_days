import random

def play_game(min_n, max_n):
    print(f"I'm thinking of a number between {min_n} and {max_n}")
    secret_number = random.randint(min_n, max_n)
    has_won = False
    
    def get_mode():
        while True:
            mode = input("choose either 'easy' or 'hard' mode.  ")
            if mode.lower() in ['easy','hard']:
                return mode.lower()
            else:
                print("please select a valid option")

    mode = get_mode()
    remaining_turns = 5 if mode == 'hard' else 10
    print(f"you have {remaining_turns} to guess the secret number!")
    while remaining_turns > 0:
        your_guess = int(input(f"make your guess ({min_n}-{max_n})  "))
        remaining_turns -= 1
        if your_guess == secret_number:
            print("you guessed correctly")
            has_won = True
            remaining_turns = 0
        elif your_guess > secret_number:
            print(f"your guess is too high. You have {remaining_turns} turns remaining")
        else:
            print(f"your guess is too low. You have {remaining_turns} turns remaining")
    if not has_won:
        print("you are out of turns. game over.")
    while True:
        play_again = input("would you like to play again? (y/n) ")
        if play_again.lower() == 'y':
            return play_game(1,100)
        elif play_again.lower() == 'n':
            print("thanks for playing.")
            return
        else:
            print("please choose 'y' or 'n'")


play_game(1,100)