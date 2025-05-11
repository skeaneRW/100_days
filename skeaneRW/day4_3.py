import random

#rock paper scissors game:
def play_game():    
    def get_selection():
        selection = input("pick your poison: rock, paper, or scissors (answer r/p/s)").lower()
        if selection in ['r','p','s']:
            return selection
        else:
            print("I didn't understand that answer")
            return get_selection()
    
    player_choice = get_selection()
    opponent_choice = random.choice(['r','p','s'])
    chosen_hands = [player_choice, opponent_choice]
    possible_results = {
        "win": [['r','s'],['p','r'],['s','p']],
        "draw": [['r','r'],['p','p'],['s','s']],
        "lose": [['s','r'],['r','p'],['p','s']],
    }
    print(f"you chose {player_choice}; your opponent chose {opponent_choice}")
    if chosen_hands in possible_results['win']:
        print('you win!')
    if chosen_hands in possible_results['draw']:
        print('it is a tie')
    if chosen_hands in possible_results['lose']:
        print('you lose!')
    
    def replay():
        play_again = input("play again? (y/n)").lower()
        if play_again in ['y','n']:
            if play_again == 'y':
                play_game()
            else:
                print('thanks for playing!')
        else:
            print("I didn't understand that answer")
            return replay()      
    replay()

play_game()
