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
            if bid_1 > bid_2:
                print(f"{name} wins with a bid of {bid_1}")
            elif bid_2 > bid_1:
                print(f"{name_2} wins with a bid of {bid_2}")
            else:
                print("it's a tie")
        elif other_players.lower() == "no":
            print("you are the only player")
            name_2 = "none"
            bid_2 = 0
            print("you win by default")
        else:
            print("please enter either 'yes' or 'no'")
        
start_game()