def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def subir():
    turn_left()
    move()

is_on_ground = True

while not at_goal():
    if is_on_ground: #se esta no chao
        if wall_in_front():
            subir()
            is_on_ground = False
        else:
            move()
    else: #se esta subindo ou descendo
        if is_facing_north(): #subindo
            if wall_on_right():
                move()
            else:
                turn_right()
                move()
                turn_right()
        else: #descendo
            if not wall_in_front():
                move()
            else:
                turn_left()
                is_on_ground = True
            
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
