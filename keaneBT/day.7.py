import random
def play_hangman():
    def get_word():
        wordbank = ["Tears", "Time", "wind", "mask", "wild", "swords", "awakening"]
        word = random.choice(wordbank)
        sloution = []
        guessed_letters = []
        for letter in word:
            sloution.append(letter)
            guessed_letters.append('-')
        return {"solution": sloution, "guessed_letters": guessed_letters}
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
    def try_2():
        yes_no = input("would you like to play again? (y/n)     ")
        if yes_no == 'y':
            play_hangman()
        elif yes_no == 'n':
            print("thanks for playing!")
        else:
            print("please choose either 'y' or 'n'")
            return try_2()
    lives = 6
    word = get_word()
    guessed_letters = []
    has_lost = False
    has_won = False 

    while not has_lost and not has_won:
        if lives < 0: 
            has_lost = True
            print ("you have lost. the word was " + ''.join(word["solution"]))
        elif (''.join(word["guessed_letters"])) == (''.join(word["solution"])):
            has_won = True
            print ("you have won! the word was " + ''.join(word["solution"]))
        else:
            guess = input("guess a letter   ")
            guessed_letters.append(guess)
            modifier = guess_letter(guess)
            lives += modifier
            if modifier == 0:
                new_clue = reveal_letters(guessed_letters)
                print(f"correct it was {' '.join(new_clue)}")
            print(f"you have {lives} lives remaining \n")
    else:
        if has_lost:
            print("you have lost hangman")
        if has_won:
            print("you have won!")
        try_2()
play_hangman()