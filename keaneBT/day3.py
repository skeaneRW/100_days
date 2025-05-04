def start_game():
    print (' you reach a road spiting in two directions, one to the left and one to the right')
    print ('you can go left or right, which way do you want to go? L/R')
    direction = input()
    if direction == 'L':
        print ('heading left you see a river your about to envestigate when you hear a noise in the distance getting louder and louder you can try to hide, rund or swim to avoid it H/R/S')
        action = input()
        if action == 'H':
            print ('you try to hide behind a tree but the only one close enough to hide behind is just a sapling. the creature sees you and you are malled to death')
        if action == 'R':
            print ('you try to run but the creature is faster than you and catches you. you are malled to death')
        if action == 'S':
            print ('you try to swim but the river is freezing cold and you are unable to swim. you die of hypothermia')
    if direction == 'R':
        print ('congrats you pick the right path and find a tresure chest full of gold and jewels, but as you aproch it you trip on a branch and fall landing on a rock and cracking your head open. you died')
    if direction =='leave' or direction == 'Leave':
        print ('congragulations you choose the secret third option to turn aruond and go home this is the best ending as you actually live')
start_game()