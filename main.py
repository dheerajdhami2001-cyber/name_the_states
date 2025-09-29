import turtle
from  state_name import  StateName

screen = turtle.Screen()
screen.title("INDIAN States Game")

image = "india.gif"
screen.addshape(image)

map_turtle = turtle.Turtle()
map_turtle.shape(image)

point = 0
state_name = StateName()
names = []
game_on = True

while game_on:
    answer_state = screen.textinput(f"{len(names)}/28 States Correct", prompt = "Which State do you want to guess?").title()
    if answer_state == "Exit":
        break
    if answer_state in state_name.all_names():
        names.append(answer_state)
        coordinate = state_name.set_coordinate(answer_state)
        state_name.move_to(coordinate,answer_state)
    if len(names) == 28:
        game_on = False



