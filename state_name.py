from idlelib.debugobj_r import remote_object_tree_item

import pandas as pd
import turtle

class StateName:
    def __init__(self):
        turtle.ht()

    def all_names(self):
        df = pd.read_csv('28_states.csv')
        return df.state.to_list()

    def set_coordinate(self,answer_state):
        df = pd.read_csv('28_states.csv')
        row = df[df.state == answer_state]
        x, y = int(row.x.iloc[0]), int(row.y.iloc[0])       # x,y = int(row.x), int(row.y) there was an error which said do this
        return x,y

    def move_to(self, coordinate, answer_state):
        turtle.teleport(*coordinate)
        turtle.write(answer_state, align='center', font=('Arial', 10, 'bold'))