def turn_right():
    turn_left()
    turn_left()
    turn_left()
def circular(): # if 
    move()
    turn_right()
    move()
    
    
while not at_goal():
    if front_is_clear():
        move()
        if at_goal():
            break
        continue
    if wall_in_front():
        turn_left()
        if front_is_clear():
            move()
            if at_goal():
                break
        turn_right()
        if wall_in_front():
            turn_left()
            move()
        else:
            break
    if front_is_clear():
        turn_left()
        if not wall_in_front():
            turn_left()
            turn_left()
            if not wall_in_front():
                circular()
                if at_goal():
                    break
                    

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
