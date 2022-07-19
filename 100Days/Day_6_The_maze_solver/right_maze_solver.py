# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    if wall_on_right() and  not front_is_clear():
        turn_left()
    if not wall_on_right() and not at_goal():
        turn_right()
        move()


# I'm afraid there should be only one case when we're creating infinite loop. Needs to be tested



## Updated version for resolveing infinite loop problem

# First idea add left_is_clear_state

# def turn_right():
#     for i in range(3):
#         turn_left()

# def left_is_clear():
#     turn_left()
#     state = front_is_clear()
#     turn_right()
#     return state
        
# while not at_goal():
#     if wall_on_right() and front_is_clear():
#         move()
#     if wall_on_right() and  not front_is_clear():
#         turn_left()
#     if left_is_clear() and right_is_clear() and not at_goal():
#         turn_left()
#         move()
#     if not wall_on_right() and not at_goal():
#         turn_right()
#         move()


##