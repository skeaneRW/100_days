# robot clears hurdle #3:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def repeat(n, fn):
    for i in range(0, n):
        fn()
def turn_right():
    repeat(3, turn_left)
        
def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    
    
while not at_goal():
    while front_is_clear():
        move()
    else:
        jump_hurdle()

# robot clears hurdle #4:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    while wall_in_front():
        turn_left()
        move()
        turn_right()
    else:
        move()
        turn_right()
        while not wall_in_front():
            move()
        turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()


# robot clears maze; by following the right wall:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
