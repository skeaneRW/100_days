#blackjack
import random
from itertools import product


class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.player_chips = 100
        self.dealer_chips = 5000
        self.bet = 0
        self.game_over = False
        self.start_game()

    def create_deck(self):
        deck = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for rank in ranks:
            for _ in range(4):
                deck.append(rank)
        random.shuffle(deck)
        return deck

    def get_player_hand(self):
        if self.game_over == False:
            if self.player_hand == []:
                for _ in range(0,2):
                    self.player_hand.append((self.deck.pop(0)))
                    self.dealer_hand.append((self.deck.pop(0)))
                print(f"your cards are {self.player_hand}; the dealer has [{(self.dealer_hand)[0], '?'}]")
            while True:
                hit = input('\nwould you like another card? (y/n) ')
                if hit == 'y':
                    self.player_hand.append(self.deck.pop(0))
                    scores = self.score('player')
                    score_message = ''
                    if len(scores) >= 2:
                        score_message = (f"your score could be {self.score('player')}")
                    elif len(scores) >= 1:
                        score_message = (f"your score is {self.score('player')[0]}")
                    else:
                        score_message = 'you are busted'
                    print(f"your cards are now {self.player_hand}; {score_message}")
                    if len(scores) == 0:
                        print(f"the dealer wins. You lose {self.bet} chips")
                        self.player_chips -= self.bet
                        self.dealer_chips += self.bet
                        return self.play_again()
                elif hit != 'n':
                    print("please choose 'y' or 'n'")
                else:
                    self.get_dealer_hand()
                    return
    
    def get_dealer_hand(self):
        dealers_score = self.score(self.dealer_hand)
        players_score = self.score(self.player_hand)
        while True:
            dealers_score = self.score('dealer')
            print(f"your hand is {self.player_hand}\ndealers hand is {self.dealer_hand}\n")
            if not dealers_score:
                print(f"dealer is bust. you win {self.bet} chips")
                self.dealer_chips -= self.bet
                self.player_chips += self.bet
                return self.play_again()
            elif max(dealers_score) > max(players_score):
                print(f"dealer wins: {max(dealers_score)} vs {max(players_score)}\nYou lose {self.bet} chips")
                self.dealer_chips += self.bet
                self.player_chips -= self.bet
                return self.play_again()
            elif max(dealers_score) == max(players_score):
                print("this round is a draw")
                return self.play_again()    
            else:
                print("dealer draws a card")
                self.dealer_hand.append((self.deck.pop(0)))

    def score(self, user):
        hand = self.dealer_hand.copy() if user == 'dealer' else self.player_hand.copy()

        def get_possible_scores(hand):
            aces = []            
            for i, card in enumerate(hand):
                if card in ['J', 'Q', 'K']:
                    hand[i] = 10
                elif card == 'A':
                    aces.append([1,11])
                    hand[i] = 0
                else:
                    hand[i] = int(card)
            possible_ace_combinations = list({sum(combination) for combination in product(*aces)})
            non_ace_total = sum([n if n != 'A' else 0 for n in hand])
            viable_ace_scores = []
            for ace_score in possible_ace_combinations:
                if ace_score + non_ace_total <= 21:
                    viable_ace_scores.append(ace_score)
            result = []
            for ace_score in viable_ace_scores:
                result.append(sum(hand) + ace_score)
            return result
        
        possible_scores = get_possible_scores(hand)
        return possible_scores
        
    def make_bet(self):
        if self.player_chips <= 0:
            print("you've lost all your chips. game over")
            self.game_over = True
            return self.restart_game()
        elif self.dealer_chips <= 0:
            print("you've brought down the house! amazing job!!!")
            self.game_over = True
            return self.restart_game()
        else:
            while True:
                player_bet = input(f"\nyou have {self.player_chips} chips available; how much do you want to bet?\n(enter a number from '1' to '{self.player_chips}' or 'q' to quit)   ")
                if player_bet.isdigit() and int(player_bet) <= self.player_chips:
                    self.bet = int(player_bet)
                    return
                elif player_bet.lower() == 'q':
                    print('thanks for playing')
                    self.game_over = True
                    return
                else:
                    print(f"you need to bet a number between 1 and {self.player_chips} chips")
    
    def play_again(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.bet = 0
        self.game_over = False
        self.start_game()

    def restart_game(self):
        while True:
            restart = input("\nWould you like to restart your game? (y/n) ")
            if restart.lower() == 'y':
                self.deck = self.create_deck()
                self.player_hand = []
                self.dealer_hand = []
                self.player_chips = 100
                self.dealer_chips = 5000
                self.bet = 0
                self.game_over = False
                return self.start_game()
            elif restart.lower() == 'n':
                print("Thanks for playing BlackJack.")
                return
            else:
                print('please choose a valid option.')

    def start_game(self):
        if self.game_over == False:
            self.make_bet()
            self.player_hand = self.get_player_hand()
        else:
            return

Blackjack()