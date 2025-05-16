def turn_right():
    turn_left()
    turn_left()
    turn_left()
def clear_maze(): 
    if at_goal():
        return
    if right_is_clear()==True:
        turn_right()
        move()
        clear_maze()
    elif front_is_clear==True:
        move()
        clear_maze()
    else :
        turn_left()
        clear_maze()
while not at_goal():
    clear_maze()
