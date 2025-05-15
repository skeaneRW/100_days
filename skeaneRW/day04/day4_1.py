import random

# heads or tails
def flip_coin():
    possible_results = ['heads', 'tails']
    i = random.randint(0,1)
    return possible_results[i]

print(flip_coin())