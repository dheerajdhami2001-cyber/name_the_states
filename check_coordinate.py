import turtle

screen = turtle.Screen()
img = "india.gif"
screen.addshape(img)

turtle.shape(img)

def get_click_coordinates(x, y):
    print(x,y)


screen.onscreenclick(get_click_coordinates)

screen.mainloop()
