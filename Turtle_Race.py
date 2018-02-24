from tkinter import *
from turtle import *
import random as rd
from winsound import *
import time as tm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def get_Width(Screen_Width):
    wWidth = None
    while wWidth is None:
        wWidth = numinput("Width", "Input Width: ", int(Screen_Width / 2), int(Screen_Width / 4),
                          int(Screen_Width - 200))
    return wWidth


def get_Height(Screen_Height):
    wHeight = None
    while wHeight is None:
        wHeight = numinput("Width", "Input Width: ", int(Screen_Height / 2), int(Screen_Height / 4),
                           int(Screen_Height - 200))
    return wHeight


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
    obj.forward(x)
    tnobj.backward(x)
    tnobj.write(name, align="left", font=("Arial", 10, "normal"))
    obj.left(180)
    return -x


def stun(obj):
    obj.left(10)
    obj.right(20)
    obj.left(10)


def TurSet(obj, color, x, y):
    obj.color(color)
    obj.shape('turtle')
    obj.penup()
    obj.goto(x, y)
    obj.right(360)


def initialize(t1, t2, t3, t4, wHeight, Screen_Width, Screen_Height):
    TurSet(t1, 'red', -(Screen_Width / 2) + 130, Screen_Height / 2 - 130)
    TurSet(t2, 'blue', -(Screen_Width / 2) + 130, Screen_Height / 2 - 130 - (wHeight / 5))
    TurSet(t3, 'green', -(Screen_Width / 2) + 130, Screen_Height / 2 - 130 - 2 * (wHeight / 5))
    TurSet(t4, 'black', -(Screen_Width / 2) + 130, Screen_Height / 2 - 130 - 3 * (wHeight / 5))


def initialize_name(tn1, tn2, tn3, tn4, wHeight, Screen_Width, Screen_Height, name_list):
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


def nameLegal(name):
    if name is None:
        return False
    if len(name) > 14:
        return False
    if name == "":
        return False
    return True


def get_name(x):
    name = None
    while not nameLegal(name):
        name = textinput("Name of turtle No." + str(x), "Please name the turtle No." + str(x) + ": ")
    return name


def naming_system(wHeight, Screen_Width, Screen_Height, tn1, tn2, tn3, tn4):
    name_list = ["", "", "", ""]
    name_list[0] = get_name(1)
    name_list[1] = get_name(2)
    name_list[2] = get_name(3)
    name_list[3] = get_name(4)
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


def winning_pose(obj, wWidth, wHeight):
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


def turtle_activity(obj, min_speed, max_speed, tnobj, name):
    rd.seed()
    RNG = rd.randint(1, 100000)
    log = 0
    if RNG < 90000:
        log = run_forward(obj, min_speed, max_speed, tnobj, name)
    elif RNG < 95000:
        log = run_backward(obj, min_speed, max_speed, tnobj, name)
    else:
        stun(obj)
    return log


def isEnd(distance_track, wWidth, start_time, time_limit):
    if distance_track[0] >= wWidth and distance_track[1] >= wWidth and distance_track[2] >= wWidth and \
            distance_track[3] >= wWidth:
        return True
    if tm.time() - start_time >= time_limit:
        return True
    return False


def race_system(wWidth, t1, t2, t3, t4, tn1, tn2, tn3, tn4, name_list, start_time):
    pass_order = [0, 0, 0, 0, 0]
    distance_track = [0, 0, 0, 0]
    time_limit = int((wWidth/20) * 2 + (wWidth)/20)
    flag = 0
    while not isEnd(distance_track, wWidth, start_time, time_limit):
        runner_list = [1, 2, 3, 4]
        runner_left = 4
        while runner_left > 0:
            rd.seed()
            runner_left -= 1
            temp = rd.randint(0, runner_left)
            temp = runner_list.pop(temp)
            if temp == 1 and distance_track[temp - 1] < wWidth:
                temp2 = turtle_activity(t1, 1, 10, tn1, name_list[0])
                distance_track[0] += temp2
                if distance_track[0] >= wWidth:
                    flag += 1
                    pass_order[temp - 1] = flag
                    if (pass_order[temp - 1] == 1) and (pass_order[4] == 0):
                        pass_order[4] = tm.time() - start_time
            elif temp == 2 and distance_track[temp - 1] < wWidth:
                temp2 = turtle_activity(t2, 1, 10, tn2, name_list[1])
                distance_track[1] += temp2
                if distance_track[1] >= wWidth:
                    flag += 1
                    pass_order[temp - 1] = flag
                    if (pass_order[temp - 1] == 1) and (pass_order[4] == 0):
                        pass_order[4] = tm.time() - start_time
            elif temp == 3 and distance_track[temp - 1] < wWidth:
                temp2 = turtle_activity(t3, 1, 10, tn3, name_list[2])
                distance_track[2] += temp2
                if distance_track[2] >= wWidth:
                    flag += 1
                    pass_order[temp - 1] = flag
                    if (pass_order[temp - 1] == 1) and (pass_order[4] == 0):
                        pass_order[4] = tm.time() - start_time
            elif temp == 4 and distance_track[temp - 1] < wWidth:
                temp2 = turtle_activity(t4, 1, 10, tn4, name_list[3])
                distance_track[3] += temp2
                if distance_track[3] >= wWidth:
                    flag += 1
                    pass_order[temp - 1] = flag
                    if (pass_order[temp - 1] == 1) and (pass_order[4] == 0):
                        pass_order[4] = tm.time() - start_time
    for i in range(4):
        if pass_order[i] == 0:
            pass_order[i] = 20
    return pass_order


def close_window(self):
    self.destroy()


def announcer(finsishTime, winner, announce_string):
    strFinsish = '{:.2f}'.format(finsishTime)
    announcePopUp = Toplevel()
    announcePopUp.title("Announcer")
    PopFrame = Frame(announcePopUp, width=250, height=150)
    PopFrame.pack_propagate(0)
    PopFrame.pack()
    announce = StringVar()
    label = Label(PopFrame, textvariable=announce, fg="red")
    announce.set(announce_string)
    label.pack()
    announceWinner = IntVar(value=winner)
    label1 = Label(PopFrame, textvariable=announceWinner, fg="blue")
    label1.pack()
    announce2 = StringVar()
    label2 = Label(PopFrame, textvariable=announce2, fg="red")
    announce2.set("Winner's finish time: ")
    label2.pack()
    announceTime = StringVar()
    label3 = Label(PopFrame, textvariable=announceTime, fg="blue")
    announceTime.set(strFinsish)
    label3.pack()
    button = Button(PopFrame, text="OK", command=announcePopUp.destroy)
    button.pack(side=TOP)


def get_Bet():
    bet = None
    while bet is None:
        bet = numinput("Bet", "Please enter the No. of the one you want to bet for: ", 1, 1, 4)
    return bet


def showChar(score, name_list, count, bet_won):
    win_graph = Toplevel()
    win_graph.title('Result graph')
    button = Button(win_graph, text="OK", command=lambda: close_window(win_graph))

    y_pos = np.arange(len(name_list))
    fig1 = plt.figure(figsize=(6, 6))
    a = fig1.add_subplot(111)
    a.bar(y_pos, score, align='center', alpha=0.5)
    plt.xticks(y_pos, name_list)
    plt.ylabel('Total Score')
    plt.xlabel('Turtle name')
    plt.title('Total Score')
    canvas1 = FigureCanvasTkAgg(fig1, master=win_graph)
    canvas1.get_tk_widget().pack(side=RIGHT)
    canvas1.draw()

    fig2 = plt.figure(figsize=(6, 6))
    b = fig2.add_subplot(111)
    b.pie([bet_won, count - bet_won], colors=['blue', 'yellow'], shadow=True, startangle=90, autopct='%1.1f%%')
    b.legend(labels=['won', 'lose'], loc="best")
    b.axis('equal')
    canvas2 = FigureCanvasTkAgg(fig2, master=win_graph)
    canvas2.get_tk_widget().pack(side=LEFT)
    canvas2.draw()

    button.pack(side=BOTTOM)


def game(t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height, score, counter, bet_won, tn1, tn2, tn3, tn4,
         name_list):
    if counter > 1:
        clear()
        wWidth = get_Width(Screen_Width)
        wHeight = get_Height(Screen_Height)
        draw_track(wWidth, wHeight, Screen_Width, Screen_Height)
    initialize_name(tn1, tn2, tn3, tn4, wHeight, Screen_Width, Screen_Height, name_list)
    initialize(t1, t2, t3, t4, wHeight, Screen_Width, Screen_Height)
    bet = get_Bet()
    start_time = tm.time()
    pass_order = race_system(wWidth, t1, t2, t3, t4, tn1, tn2, tn3, tn4, name_list, start_time)
    score[0] += (wWidth / 10) / pass_order[0]
    score[1] += (wWidth / 10) / pass_order[1]
    score[2] += (wWidth / 10) / pass_order[2]
    score[3] += (wWidth / 10) / pass_order[3]
    winner = 0
    for i in range(4):
        if pass_order[i] == 1:
            winner = i + 1
    if pass_order[int(bet - 1)] == 1:
        announcer(pass_order[4], winner, "You won >w<\nWinner is turtle number: ")
        bet_won += 1
    else:
        announcer(pass_order[4], winner, "You lose :'<\nWinner is turtle number: ")
    if pass_order[0] == 1:
        winning_pose(t1, wWidth, wHeight)
    elif pass_order[1] == 1:
        winning_pose(t2, wWidth, wHeight)
    elif pass_order[2] == 1:
        winning_pose(t3, wWidth, wHeight)
    else:
        winning_pose(t4, wWidth, wHeight)
    print(score)
    print(counter)
    print(bet_won)
    showChar(score, name_list, counter, bet_won)
    return bet_won


def restart(self, t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height, score, counter, bet_won,  tn1, tn2, tn3,
            tn4, name_list):
    self.destroy()
    PlaySound(None, SND_ASYNC)
    PlaySound("Sound01.wav", SND_ASYNC + SND_LOOP)
    bet_won = game(t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height, score, counter, bet_won, tn1, tn2, tn3,
                   tn4, name_list)
    RestartPopUp = Toplevel()
    RestartPopUp.title("Restart ?")
    root1Frame = Frame(RestartPopUp, width=270, height=50)
    root1Frame.pack_propagate(0)
    root1Frame.pack()
    restart_button = Button(root1Frame, text="Restart", fg="black",
                            command=lambda: restart(RestartPopUp, t1, t2, t3, t4, wWidth, wHeight, Screen_Width,
                                                    Screen_Height, score, counter + 1, bet_won, tn1, tn2, tn3, tn4,
                                                    name_list))
    restart_button.pack(side=TOP)
    quit_button = Button(root1Frame, text="Quit", fg="red", command=quit)
    quit_button.pack(side=TOP)


def Start(self):
    PlaySound("Sound01.wav", SND_ASYNC + SND_LOOP)
    self.destroy()
    score = [0, 0, 0, 0]
    bet_won = 0
    counter = 1
    Screen_Width = 800
    Screen_Height = 600
    wWidth = get_Width(Screen_Width)
    wHeight = get_Height(Screen_Height)
    draw_track(wWidth, wHeight, Screen_Width, Screen_Height)
    tn1, tn2, tn3, tn4 = Turtle(), Turtle(), Turtle(), Turtle()
    tn1.hideturtle()
    tn2.hideturtle()
    tn3.hideturtle()
    tn4.hideturtle()
    name_list = naming_system(wHeight, Screen_Width, Screen_Height, tn1, tn2, tn3, tn4)
    t1, t2, t3, t4 = Turtle(), Turtle(), Turtle(), Turtle()
    bet_won = game(t1, t2, t3, t4, wWidth, wHeight, Screen_Width, Screen_Height, score, counter, bet_won, tn1, tn2, tn3,
                   tn4, name_list)
    RestartPopUp = Toplevel()
    RestartPopUp.title("Restart ?")
    root1Frame = Frame(RestartPopUp, width=270, height=50)
    root1Frame.pack_propagate(0)
    root1Frame.pack()
    restart_button = Button(root1Frame, text="Restart", fg="black",
                            command=lambda: restart(RestartPopUp, t1, t2, t3, t4, wWidth, wHeight, Screen_Width,
                                                    Screen_Height, score, counter + 1, bet_won, tn1, tn2, tn3, tn4,
                                                    name_list))
    restart_button.pack(side=TOP)
    quit_button = Button(root1Frame, text="Quit", fg="red", command=quit)
    quit_button.pack(side=TOP)


def showAbout():
    aboutWindow = Toplevel()
    aboutWindow.title("About")
    subFrame = Frame(aboutWindow, width=220, height=160)
    subFrame.pack_propagate(0)
    subFrame.pack()
    member_name = StringVar()
    label = Label(subFrame, textvariable=member_name)
    member_name.set(
        "Team Leader: \nPhạm Hoàng Anh Tuấn\nDeveloper + QA: \nNguyễn Hoàng Việt\nLê Quốc Việt\n Artist: "
        "\nMai Bảo Trân")
    label.pack()
    button = Button(subFrame, text="OK", command=aboutWindow.destroy)
    button.pack()


def main():
    root = Tk()
    root.title("Turtle Race Game")
    mainFrame = Frame(root, bg="white", width=270, height=220)
    mainFrame.pack_propagate(0)
    mainFrame.pack()
    start_button = Button(mainFrame, text="Start", fg="black", command=lambda: Start(root))
    start_button.pack(side=TOP)
    about_button = Button(mainFrame, text="About", fg="blue", command=lambda: showAbout())
    about_button.pack(side=TOP)
    quit_button = Button(mainFrame, text="Quit", fg="red", command=quit)
    quit_button.pack(side=TOP)
    image = PhotoImage(file="TeamLogo.gif")
    label = Label(mainFrame, image=image, bg="white")
    label.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
