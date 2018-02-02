from turtle import *
from random import randint


def draw_track():
    hideturtle()
    penup()
    speed(0)
    goto(-(Screen_width / 2) + 100, Screen_height / 2 - 50)
    for count in range(int(width/20)):
        write(count, align='center')
        right(90)
        forward(10)
        pendown()
        for count2 in range(int(height/20)):
            forward(10)
            penup()
            forward(10)
            pendown()
        penup()
        backward(height + 10)
        left(90)
        forward(20)


def initialize(obj, color, x, y):
    obj.color(color)
    obj.shape('turtle')
    obj.penup()
    obj.goto(x, y)
    obj.right(360)


def naming_system():
    name_list = []
    name_list.append(textinput("Name of turtle 1", "Please name the turtle No.1: "))
    name_list.append(textinput("Name of turtle 2", "Please name the turtle No.2: "))
    name_list.append(textinput("Name of turtle 3", "Please name the turtle No.3: "))
    name_list.append(textinput("Name of turtle 4", "Please name the turtle No.4: "))
    goto(-(Screen_width / 2) + 30, Screen_height / 2 - 110)
    write(name_list[0], align="left", font=("Arial", 10, "normal"))
    goto(-(Screen_width / 2) + 30, Screen_height / 2 - 110 - height / 5)
    write(name_list[1], align="left", font=("Arial", 10, "normal"))
    goto(-(Screen_width / 2) + 30, Screen_height / 2 - 110 - 2 * height / 5)
    write(name_list[2], align="left", font=("Arial", 10, "normal"))
    goto(-(Screen_width / 2) + 30, Screen_height / 2 - 110 - 3 * height / 5)
    write(name_list[3], align="left", font=("Arial", 10, "normal"))


def run_forward(obj, min_speed, max_speed):
    obj.forward(randint(min_speed, max_speed))


def run_backward(obj, min_speed, max_speed):
    obj.left(180)
    obj.backward(randint(min_speed, max_speed))
    obj.right(180)


def idle(obj):
    obj.left(10)
    obj.right(20)
    obj.left(10)


Screen_width = 800
Screen_height = 600
setup(width=Screen_width, height=Screen_height)
width = numinput("Width", "Please type in your desire width for the race track: ", Screen_width/2, Screen_width/4, Screen_width - 100)
height = numinput("Height", "Please type in your desire height for the race track: ", Screen_height/2, Screen_height/4, Screen_height - 100)
draw_track()
t1, t2, t3, t4 = Turtle(), Turtle(), Turtle(), Turtle()
initialize(t1, 'red', -(Screen_width / 2) + 80, Screen_height / 2 - 100)
initialize(t2, 'blue', -(Screen_width / 2) + 80, Screen_height / 2 - 100 - height/5)
initialize(t3, 'green', -(Screen_width / 2) + 80, Screen_height / 2 - 100 - 2*height/5)
initialize(t4, 'yellow', -(Screen_width / 2) + 80, Screen_height / 2 - 100 - 3*height/5)
naming_system()
done()

