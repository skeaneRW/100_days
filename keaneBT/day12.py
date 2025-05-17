import random
def start_game():
    turns=10
    sec_num=random.randint(1,100)
    Lv=input ('hard or easy H/E').lower()
    if Lv=='h':
        turns-=5
    while True:
        guess=input ('pick a numeber between 1 and 100')
        if guess.isdigit():
            guess=int(guess)
        else:
            print ('please enter a number')
            continue
        if guess > sec_num:
            turns-=1
            if turns==0:
                print ('game over')
                return
            print(f'too high you have {turns} tries left')
        if guess < sec_num:
            turns-=1 
            if turns==0:
                print ('game over')
                return
            print (f'too low you have {turns} tries left')
        if guess == sec_num:
            print("you win")
            return
        if guess == 'exit':
            print ('thank you for playing')
            return
start_game()