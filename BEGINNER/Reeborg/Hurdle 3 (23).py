def turn_right():
    turn_left()
    turn_left()
    turn_left()
def circular(): # if 
    move()
    turn_right()
    move()
def Checkleft():
    turn_left()
    if not wall_in_front():
        turn_right
        return true
    else:
        return false
def Checkright():
    turn_right()
    if not wall_in_front():
        turn_left
        return true
    else:
        return false
    
    

if front_is_clear():
    move()
    
while not at_goal():
    if wall_in_front():
        if Checkleft() and Checkright():
            turn_right()
            circular()
        if Checkleft():
            turn_left()
            move()
        if Checkright():
            turn_right()
            move()
    if front_is_clear():
        if not Checkright() and not Checkleft():
            move()
        if not Checkright():
            move()
        if not Checkleft():
            move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
