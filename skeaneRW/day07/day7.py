#hangman
import random

def play_hangman():
    def get_word():
        wordbank = ["rhyme", "sombrero", "lasso", "rhombus", "orchid", "medusa", "silent", "filling"]
        word = random.choice(wordbank)
        solution = []
        guessed_letters = []
        for letter in word:
            solution.append(letter)
            guessed_letters.append('-')
        return {"solution": solution, "guessed_letters": guessed_letters}

    def guess_letter(guess):
        if guess in word["solution"]:
            return 0
        else:
            return -1
        
    def reveal_letters(guessed_letters):
        new_guessed_letters = word["guessed_letters"]
        for letter in guessed_letters:
            for idx, letter in enumerate(word["solution"]):
                if letter == guess:
                    new_guessed_letters[idx] = letter
        return new_guessed_letters
    
    def play_again():
        yes_no = input("would you like to play again? (y/n)     ")
        if yes_no == 'y':
            play_hangman()
        elif yes_no == 'n':
            print("thanks for playing!")
        else:
            print("please choose either 'y' or 'n'")
            return play_again()

    lives = 6
    word = get_word()
    has_lost = False
    has_won = False
    guessed_letters = []

    while not has_lost and not has_won:
        if lives < 1: 
            has_lost = True
        elif (''.join(word["guessed_letters"])) == (''.join(word["solution"])): 
            has_won = True
        else:
            guess = input("guess a letter   ")
            guessed_letters.append(guess)
            modifier = guess_letter(guess)
            lives += modifier
            if modifier == 0:
                new_clue = reveal_letters(guessed_letters)
                print(f"great guess! The word is {' '.join(new_clue)}")
            print(f"you have {lives} lives remaining \n")
    else:
        if has_lost:
            print("you have lost hangman")
        if has_won:
            print("you have won!")
        play_again()
    return

play_hangman()