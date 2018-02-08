import _tkinter
from tkinter import *
from turtle import *
import random as rd
from winsound import *


def draw_track(wWidth, wHeight, Screen_Width, Screen_Height):
    speed(0)
    hideturtle()
    penup()
    goto(-Screen_Width / 2 + 150, Screen_Height / 2 - 100)
    for count in range(int(wWidth / 20)):
        write(count, align='center')
        right(90)
        forward(10)
        pendown()
        for count2 in range(int(wHeight / 20)):
            forward(10)
            penup()
            forward(10)
            pendown()
        penup()
        backward(int(wHeight / 20) * 20 + 10)
        left(90)
        forward(20)


def run_forward(obj, min_speed, max_speed, tnobj, name):
    rd.seed()
    x = rd.randint(min_speed, max_speed)
    obj.forward(x)
    tnobj.clear()
    tnobj.forward(x)
    tnobj.write(name, align="left", font=("Arial", 10, "normal"))
    return x


def run_backward(obj, min_speed, max_speed, tnobj, name):
    rd.seed()
    x = rd.randint(min_speed, max_speed)
    obj.left(180)
    tnobj.clear()
    obj.backward(x)
    tnobj.backward(x)
    tnobj.write(name, align="left", font=("Arial", 10, "normal"))
    obj.left(180)
    return x


def stun(obj):
    obj.left(10)
    obj.right(20)
    obj.left(10)


def set(obj, color, x, y):
    obj.color(color)
    obj.shape('turtle')
    obj.penup()
    obj.goto(x, y)
    obj.right(360)


def initialize(t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height):
    set(t1, 'red', -(Screen_Width / 2) + 130, Screen_Height / 2 - 130)
    set(t2, 'blue', -(Screen_Width / 2) + 130, Screen_Height / 2 - 130 - (wHeight / 5))
    set(t3, 'green', -(Screen_Width / 2) + 130, Screen_Height / 2 - 130 - 2 * (wHeight / 5))
    set(t4, 'yellow', -(Screen_Width / 2) + 130, Screen_Height / 2 - 130 - 3 * (wHeight / 5))


def initialize_name(tn1, tn2, tn3, tn4, wWidth, wHeight, Screen_Width, Screen_Height, name_list):
    tn1.clear()
    tn2.clear()
    tn3.clear()
    tn4.clear()
    tn1.goto(-(Screen_Width / 2) + 80, Screen_Height / 2 - 130)
    tn2.goto(-(Screen_Width / 2) + 80, Screen_Height / 2 - 130 - wHeight / 5)
    tn3.goto(-(Screen_Width / 2) + 80, Screen_Height / 2 - 130 - 2 * wHeight / 5)
    tn4.goto(-(Screen_Width / 2) + 80, Screen_Height / 2 - 130 - 3 * wHeight / 5)
    tn1.write(name_list[0], align="left", font=("Arial", 10, "normal"))
    tn2.write(name_list[1], align="left", font=("Arial", 10, "normal"))
    tn3.write(name_list[2], align="left", font=("Arial", 10, "normal"))
    tn4.write(name_list[3], align="left", font=("Arial", 10, "normal"))

def naming_system(wWidth, wHeight, Screen_Width, Screen_Height, tn1, tn2, tn3, tn4):
    name_list = ["", "", "", ""]
    name_list[0] = textinput("Name of turtle 1", "Please name the turtle No.1: ")
    if name_list[0] == "":
        name_list[0] = "Bob"
    name_list[1] = textinput("Name of turtle 2", "Please name the turtle No.2: ")
    if name_list[1] == "":
        name_list[1] = "Alice"
    name_list[2] = textinput("Name of turtle 3", "Please name the turtle No.3: ")
    if name_list[2] == "":
        name_list[2] = "Alisa"
    name_list[3] = textinput("Name of turtle 4", "Please name the turtle No.4: ")
    if name_list[3] == "":
        name_list[3] = "Dave"
    tn1.penup()
    tn2.penup()
    tn3.penup()
    tn4.penup()
    tn1.goto(-(Screen_Width / 2) + 80, Screen_Height / 2 - 130)
    tn1.write(name_list[0], align="left", font=("Arial", 10, "normal"))
    tn2.goto(-(Screen_Width / 2) + 80, Screen_Height / 2 - 130 - wHeight / 5)
    tn2.write(name_list[1], align="left", font=("Arial", 10, "normal"))
    tn3.goto(-(Screen_Width / 2) + 80, Screen_Height / 2 - 130 - 2 * wHeight / 5)
    tn3.write(name_list[2], align="left", font=("Arial", 10, "normal"))
    tn4.goto(-(Screen_Width / 2) + 80, Screen_Height / 2 - 130 - 3 * wHeight / 5)
    tn4.write(name_list[3], align="left", font=("Arial", 10, "normal"))
    return name_list


def winning_pose(obj, tnobj, wWidth, wHeight):
    PlaySound(None, SND_ASYNC)
    PlaySound("Sound02.wav", SND_ASYNC + SND_LOOP)
    obj.penup()
    obj.goto(0,0)
    obj.left(20)
    obj.right(40)
    obj.left(20)
    obj.left(360)
    obj.right(360)
    obj.circle((wWidth + wHeight)/2)
    obj.right(90)
    obj.circle(wWidth)
    obj.right(90)
    obj.circle(wHeight)
    obj.right(180)


def turtle_activity(obj, min_speed, max_speed, wWidth, tnobj, name):
    rd.seed()
    RNG = rd.randint(1, 100000)
    log = 0
    if RNG < 99900:
        log = run_forward(obj, min_speed, max_speed, tnobj, name)
    elif RNG < 99950:
        log = run_backward(obj, min_speed, max_speed, tnobj, name)
    else:
        stun(obj)
    return log


def isEnd(distance_track, wWidth, turn, turn_limit):
    if distance_track[0] > wWidth and distance_track[1] > wWidth and distance_track[2] > wWidth and distance_track[
        3] > wWidth:
        return True
    if turn >= turn_limit:
        return True
    return False


def race_system(wWidth, wHeight, t1, t2, t3, t4, tn1, tn2, tn3, tn4, name_list):
    pass_order = [0, 0, 0, 0]
    distance_track = [0, 0, 0, 0]
    turn_limit = wWidth * 2
    turn = 0
    flag = 0
    while not isEnd(distance_track, wWidth, turn, turn_limit):
        runner_list = [1, 2, 3, 4]
        runner_left = 4
        while runner_left > 0:
            rd.seed()
            runner_left -= 1
            temp = rd.randint(0, runner_left)
            temp = runner_list.pop(temp)
            if temp == 1 and distance_track[temp - 1] < wWidth:
                temp2 = turtle_activity(t1, 1, 10, wWidth, tn1, name_list[0])
                distance_track[0] += temp2
                if distance_track[0] >= wWidth:
                    flag += 1
                    pass_order[temp - 1] = flag
            elif temp == 2 and distance_track[temp - 1] < wWidth:
                temp2 = turtle_activity(t2, 1, 10, wWidth, tn2, name_list[1])
                distance_track[1] += temp2
                if distance_track[1] >= wWidth:
                    flag += 1
                    pass_order[temp - 1] = flag
            elif temp == 3 and distance_track[temp - 1] < wWidth:
                temp2 = turtle_activity(t3, 1, 10, wWidth, tn3, name_list[2])
                distance_track[2] += temp2
                if distance_track[2] >= wWidth:
                    flag += 1
                    pass_order[temp - 1] = flag
            elif temp == 4 and distance_track[temp - 1] < wWidth:
                temp2 = turtle_activity(t4, 1, 10, wWidth, tn4, name_list[3])
                distance_track[3] += temp2
                if distance_track[3] >= wWidth:
                    flag += 1
                    pass_order[temp - 1] = flag
        turn += 1
    return pass_order


def close_window(self):
    self.destroy()


def win_announce():
    root2 = Toplevel()
    frame = Frame(root2, width=50, height=50)
    frame.pack()
    txt = Text(frame, width=30, height=10)
    txt.tag_configure("center", justify='center')
    txt.insert(INSERT, "You Won >w<")
    txt.tag_add("center", "1.0", "end")
    OK_button = Button(frame, text="OK", command=lambda: close_window(root2))
    OK_button.pack(side=BOTTOM)
    txt.pack()


def loose_announce():
    root2 = Toplevel()
    frame = Frame(root2, width=50, height=50)
    frame.pack()
    txt = Text(frame, width=30, height=10)
    txt.tag_configure("center", justify='center')
    txt.insert(INSERT, "You lost :<")
    txt.tag_add("center", "1.0", "end")
    OK_button = Button(frame, text="OK", command=lambda: close_window(root2))
    OK_button.pack(side=BOTTOM)
    txt.pack()


def game(t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height, score, counter, bet_won, tn1, tn2, tn3, tn4, name_list):
    if counter > 0:
        clear()
        wWidth = int(
            numinput("Width", "Input Width: ", int(Screen_Width / 2), int(Screen_Width / 4), int(Screen_Width - 200)))
        wHeight = int(
            numinput("Height", "Input Height: ", int(Screen_Height / 2), int(Screen_Height / 4),
                     int(Screen_Height - 100)))
        draw_track(wWidth, wHeight, Screen_Width, Screen_Height)
    bet = numinput("Bet", "Please enter the No. of the one you want to bet for: ", 1, 1, 4)
    initialize_name(tn1, tn2, tn3, tn4, wWidth, wHeight, Screen_Width, Screen_Height, name_list)
    initialize(t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height)
    pass_order = race_system(wWidth, wHeight, t1, t2, t3, t4, tn1, tn2, tn3, tn4, name_list)
    score[0] += (wWidth / 10) / pass_order[0]
    score[1] += (wWidth / 10) / pass_order[1]
    score[2] += (wWidth / 10) / pass_order[2]
    score[3] += (wWidth / 10) / pass_order[3]
    if pass_order[int(bet - 1)] == 1:
        win_announce()
        bet_won += 1
    else:
        loose_announce()
    if pass_order[0] == 1:
        winning_pose(t1, tn1, wWidth, wHeight)
    elif pass_order[1] == 1:
        winning_pose(t2, tn2, wWidth, wHeight)
    elif pass_order[2] == 1:
        winning_pose(t3, tn3, wWidth, wHeight)
    else:
        winning_pose(t4, tn4, wWidth, wHeight)
    print(score)
    print(counter)
    print(bet_won)


def restart(self, t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height, score, counter, bet_won,  tn1, tn2, tn3, tn4, name_list):
    self.destroy()
    PlaySound(None, SND_ASYNC)
    PlaySound("Sound01.wav", SND_ASYNC + SND_LOOP)
    game(t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height, score, counter, bet_won, tn1, tn2, tn3, tn4,
         name_list)
    root1 = Toplevel()
    restart_button = Button(root1, text="Restart", fg="red",
                            command=lambda: restart(root1, t1, t2, t3, t4, wWidth, wHeight, Screen_Width,
                                                    Screen_Height, score, counter + 1, bet_won, tn1, tn2, tn3, tn4, name_list))
    restart_button.pack(side=TOP)
    quit_button = Button(root1, text="Quit", fg="black", command=quit)
    quit_button.pack(side=BOTTOM)
    # root1.mainloop()


def Start(self):
    PlaySound("Sound01.wav", SND_ASYNC + SND_LOOP)
    self.destroy()
    score = [0, 0, 0, 0]
    bet_won = 0
    counter = 0
    Screen_Width = 800
    Screen_Height = 600
    wWidth = int(
        numinput("Width", "Input Width: ", int(Screen_Width / 2), int(Screen_Width / 4), int(Screen_Width - 200)))
    wHeight = int(
        numinput("Height", "Input Height: ", int(Screen_Height / 2), int(Screen_Height / 4), int(Screen_Height - 100)))
    draw_track(wWidth, wHeight, Screen_Width, Screen_Height)
    tn1, tn2, tn3, tn4 = Turtle(), Turtle(), Turtle(), Turtle()
    tn1.hideturtle()
    tn2.hideturtle()
    tn3.hideturtle()
    tn4.hideturtle()
    name_list = naming_system(wWidth, wHeight, Screen_Width, Screen_Height, tn1, tn2, tn3, tn4)
    t1, t2, t3, t4 = Turtle(), Turtle(), Turtle(), Turtle()
    game(t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height, score, counter, bet_won, tn1, tn2, tn3, tn4, name_list)
    root1 = Toplevel()
    restart_button = Button(root1, text="Restart", fg="black",
                            command=lambda: restart(root1, t1, t2, t3, t4, wWidth, wHeight, Screen_Width,
                                                    Screen_Height, score, counter + 1, bet_won, tn1, tn2, tn3, tn4, name_list))
    restart_button.pack(side=TOP)
    quit_button = Button(root1, text="Quit", fg="red", command=quit)
    quit_button.pack(side=BOTTOM)
    # root1.mainloop()


def main():
    root = Tk()
    start_button = Button(root, text="Start", fg="black", command=lambda: Start(root))
    start_button.pack(side=TOP)
    quit_button = Button(root, text="Quit", fg="black", command=quit)
    quit_button.pack(side=BOTTOM)
    root.mainloop()


if __name__ == '__main__':
    main()
