'''
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
'''

import pandas

def get_nato_word():
    df = pandas.read_csv("skeaneRW/day30/nato/nato_phonetic_alphabet.csv")
    nato_dict = {row.letter:row.code for _, row in df.iterrows()}
    try:
        word = input("enter your word:  ")
        for char in word:
            if char.upper() not in nato_dict:
                raise ValueError
    except ValueError as err:
        print("please only include letters in your word")
        return get_nato_word()
    nato_name_list = [nato_dict[l.upper()] for l in word]
    print(nato_name_list)

run_nato = True
while run_nato:
    get_nato_word()
    def check_replay():
        replay_opt = input("would you like to do another word? (y/n)? ")
        if replay_opt.lower() == 'n':
            print('thanks for using the NATO encoder')
            global run_nato
            run_nato = False 
            return
        if replay_opt.lower() not in ['y', 'n']:
            print(f"this is not a valid option. please choose y or n only.")
            check_replay()
    check_replay()
            