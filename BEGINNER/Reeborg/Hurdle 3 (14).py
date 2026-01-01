def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        turn_left()
        if front_is_clear():
            move()
        if wall_in_front():
            turn_right()

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
