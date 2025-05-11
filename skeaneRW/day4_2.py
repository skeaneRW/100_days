import random

# bankers roulette-- pick a random number from the list of people.
def get_name():
    people = ["Stephen", "Kate", "Isobel", "Liam", "Brendan", "Juliet"]
    return random.choice(people)

lucky_one = get_name()
print(lucky_one)

