from turtle import *
from random import *
from winsound import *


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
    seed()
    x = randint(min_speed, max_speed)
    obj.forward(x)
    return x


def run_backward(obj, min_speed, max_speed):
    seed()
    x = randint(min_speed, max_speed)
    obj.left(180)
    obj.backward(x)
    obj.right(180)
    return x


def idle(obj):
    obj.left(10)
    obj.right(20)
    obj.left(10)


def sound_system():
    PlaySound('sound.wav', SND_ASYNC + SND_LOOP)


def stop_check(distance_list, turn, turn_limit):
    if distance_list[0] > width and distance_list[1] > width and distance_list[2] > width and distance_list[3] > width:
        return True
    if turn > turn_limit:
        return True
    return False


def turtle_run(obj, distance_list, no):
    seed()
    flag = randint(1, 1000)
    if flag <= 800:
        distance_list[no-1] += run_forward(obj, 1, 10)
    elif flag > 800 and flag < 900:
        distance_list[no-1] += run_backward(obj, 1, 10)
    else:
        idle(obj)
    if distance_list[no-1] > width:
        return 1
    return 0

#random order will be add later, please note
def racing_system(order_list):
    flag = 0
    turn_limit = width
    distance_list = [0, 0, 0, 0]
    order_list = [0, 0, 0, 0]
    runner = 0
    turn = 0
    while not stop_check(distance_list, turn, turn_limit):
        seed()
        n = 3
        run_queue = [1, 2, 3, 4]
        while n >= 0:
            runner = randint(0, n)
            temp = run_queue.pop(runner)
            if temp == 1 and distance_list[temp-1] < width:
                flag += turtle_run(t1, distance_list, temp)
                order_list[temp - 1] = flag
            elif temp == 2 and distance_list[temp-1] < width:
                flag += turtle_run(t2, distance_list, temp)
                order_list[temp - 1] = flag
            elif temp == 3 and distance_list[temp-1] < width:
                flag += turtle_run(t3, distance_list, temp)
                order_list[temp - 1] = flag
            elif temp == 4 and distance_list[temp-1] < width:
                flag += turtle_run(t4, distance_list, temp)
                order_list[temp - 1] = flag
            turn += 1
            n -= 1


sound_system()
Screen_width = 800
Screen_height = 600
setup(width=Screen_width, height=Screen_height)
width = numinput("Width", "Please type in your desire width for the race track: ", Screen_width/2, Screen_width/4, Screen_width - 100)
height = numinput("Height", "Please type in your desire height for the race track: ", Screen_height/2, Screen_height/4, Screen_height - 100)
#draw_track()
t1, t2, t3, t4 = Turtle(), Turtle(), Turtle(), Turtle()
initialize(t1, 'red', -(Screen_width / 2) + 80, Screen_height / 2 - 100)
initialize(t2, 'blue', -(Screen_width / 2) + 80, Screen_height / 2 - 100 - height/5)
initialize(t3, 'green', -(Screen_width / 2) + 80, Screen_height / 2 - 100 - 2*height/5)
initialize(t4, 'yellow', -(Screen_width / 2) + 80, Screen_height / 2 - 100 - 3*height/5)
name_list = []
#naming_system()
score_list = [0, 0, 0, 0]
#bet = numinput("Bet", "Please input the number order of the turtle that you want to bet on: ", 1, 1, 4)
order_list = [0, 0, 0, 0]
racing_system(order_list)
done()

