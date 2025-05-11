import random
def game():

    def get_user_choice():
        user_input = input("Enter your choice (r, p, s) ").lower()
        if user_input == 'r':
            return 1
        elif user_input == 'p':
            return 2
        elif user_input == 's':
            return 3
        else:
            print("Invalid input. Please enter r, p, or s")
            return get_user_choice()

    def get_computer_choice():
        return random.randint(1, 3)

    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            return "You win!"
        else:
            return "You lose!"

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        list_of_choices = ['rock', 'paper', 'scissors']
        print(f"Your choice: {list_of_choices[user_choice]} computer's choice: {list_of_choices[computer_choice]}")
        print(result)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
game()