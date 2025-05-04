# Adventure game: make a simple text-based adventure game with a few rooms and items to collect.

ascii_art = """
               __====-_  _-====___
      _--^^^#####//      \\#####^^^--_
   _-^##########// (    ) \\##########^-_
  -############//  |\^^/|  \\############-
 /############//   ( oo )   \\############\
|#############((    (__)    ))#############|
|###############\\  /  \   //###############|
|################\\/ (_)\ //################|
 \########/         |||||        \########/
   ----              |||             ----
       ADVENTURE GAME by STEPHEN KEANE
         \_____     |||     _____/
               \____|||____/
                    |||
                 .-'   '-.
                /         \
               | $$$$$$$$$ |
                \_________/
"""

def launch_game():
    print(ascii_art)
    print("Welcome to the Adventure Game!")
    print_story("You find at a clearing in the woods. Paths veer off in two directions.")
    direction = input("Do you want to go left or right? (answer: left/right) ").lower()
    if direction == "left":
        explore_left_path()
    elif direction == "right":
        explore_right_path()
    else:
        print("Invalid choice! Please choose 'left' or 'right'.")
        launch_game()

def play_again():
    response = input("Do you want to play again? (answer: y/n) ").lower()
    if response == "y":
        launch_game()
    elif response == "n":
        print("Thanks for playing! Goodbye!")
    else:
        print("I'm sorry I didn't understand that.")
        play_again()

def print_story(story):
    print("\n")
    print(story)
    print("\n\n")

def explore_left_path():
    print_story("the left path leads you to a dark cave. It's spooky and dark and your flashlight is running low. Do you try to make a fire or keep going?")
    print("\n\n")
    choice = input("Do you want to make a fire or keep going? (answer: fire/keep going) ").lower()
    if choice == "fire":
        make_fire()
    elif choice == "keep going":
        explore_in_the_dark()
    else:
        print("Invalid choice! Please choose 'fire' or 'keep going'.")
        explore_left_path()

def explore_right_path():
    print_story("you have hit a dead end!")
    play_again()

def make_fire():
    print_story("you are able to make a fire, but the light attracts a warty ogre. The ogre eats you. you're dead.")
    play_again()

def explore_in_the_dark():
    print_story("You stumble around in the dark for a bit, but manage to find your way to a subterranan lake. light filters down from above. There appears to be something at the bottom of the lake. There's a boat at the edge of the water. You hear an angry grunty noise behind you.")
    choice = input("What will you do? Investigate the noise, dive into the lake or use the boat? (answer: noise/dive/boat) ").lower()
    if choice == "noise":
        investigate_noise()
    elif choice == "dive":
        dive_into_lake()
    elif choice == "boat":
        use_boat()
    else:
        print("Invalid choice! Please choose 'noise', 'dive', or 'boat'.")
        explore_in_the_dark()
def investigate_noise():
    print_story("You turn around to investigate the noise and find a seeminly harmless frog. You pick it up and it spits venom in your face. You are dead.")
    play_again()

def dive_into_lake():
    print_story("You dive into the lake and swim down to the bottom. You find a treasure chest! You open the chest and find gold coins and jewels. You swim back to the surface with your treasure.")
    print("Congratulations! You've found the treasure and escaped the cave!")
    play_again()

def use_boat():
    print_story("Good news! There's a pile of treasure in the boat! Bad news! It's cursed and you can never leave the lake. You are trapped forever.")
    play_again()

launch_game()
