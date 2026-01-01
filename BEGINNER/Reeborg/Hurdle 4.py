def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def Checkleft():
    turn_left()
    if not wall_in_front():
        turn_right()
        return True
    else:
        turn_right()
        return False
def Checkright():
    turn_right()
    if not wall_in_front():
        turn_left()
        return True
    else:
        turn_left()
        return False

def Clearleft():
    turn_left()
    if front_is_clear():
        turn_right()
        return True
    else:
        turn_right()
        return False
def Clearright():
    turn_right()
    if front_is_clear():
        turn_left()
        return True
    else:
        turn_left()
        return False
def jump():
    turn_left()
    move()
    
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
while not at_goal():
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
