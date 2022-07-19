## This is the solution of puzzles from site:

# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def turn_right():
    for i in range(3):
        turn_left()
        
def turn_around():        
    for i in range(2):
        turn_left()        
def draw_square():
    for i in range(4):
        move()
        turn_left()
def draw_more_right_way_square():
    turn_left()
    move()

    for i in range(3):
        turn_right()
        move()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def short_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def jump_over_the_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right() and not wall_in_front():
        move()
    turn_left()
    
    
    
def resolve():
    for i in range(6):
        jump()

def resolve2():
    while not(at_goal()):
        jump()
def resolve3():
    while not(at_goal()):
        if front_is_clear():
            move()
        if wall_in_front():
            short_jump()
            
def resolve4():
    while not(at_goal()):
        if front_is_clear():
            move()
        if wall_in_front():
            jump_over_the_wall()
              
    
#draw_more_right_way_square()
resolve4()
