def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        turn_left()
    elif wall_in_front():
        turn_right()
    if not wall_in_front:
        move()

    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
