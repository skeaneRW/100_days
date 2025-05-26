'''
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
'''

import pandas
df = pandas.read_csv("skeaneRW/day26/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for _, row in df.iterrows()}
word = input("enter your word:  ")
nato_name_list = [nato_dict[l.upper()] for l in word]
print(nato_name_list)