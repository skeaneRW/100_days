import random
def start_game():
        print("welcome what's your name?")
        name = input("Enter your name: ")
        print("what's your bid?")
        bid_1 = input("Enter your bid: ")
        bid_1 = int(bid_1)
        print("are there any other players? (yes/no)")  
        other_players = input("Enter yes or no: ")
 if other_players.lower() == "yes":
        print ("what is your name?")
        name_2 = input("Enter your name: ")
        print("what's your bid?")
        bid_2 = input("Enter your bid: ")
        bid_2 = int(bid_2)
    elif other_players.lower() == "no":
        if bid_1 > bid_2:


        start_game()