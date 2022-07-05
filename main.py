import random
import math
import time


from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('600x400')
root.title('Maths Tester')
minute = StringVar()
second = StringVar()
minute.set("00")
second.set("00")
minuteEntry = Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=180, y=20)


def submit():
    try:
        temp = int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        if mins > 60:
            hours, mins = divmod(mins, 60)
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
        temp -= 1
btn = Button(root, text='Set Time Countdown', bd='5',
             command=submit)
btn.place(x=70, y=120)
root.mainloop()

groundtruth = 0
userans = 0
score = 0


def answerer():
    if userans == groundtruth:
        print('Correct')
        global score
        score += 1
    else:
        print('Incorrect, the correct answer was', groundtruth)


def myadder():
    int1 = random.randint(1, 100)
    int2 = random.randint(1, 100)
    global groundtruth
    groundtruth = int1 + int2
    print("What is", int1, '+', int2, '?')
    global userans
    userans = int(input())


def mymultiple():
    int1 = random.randint(1, 100)
    int2 = random.randint(1, 100)
    global groundtruth
    groundtruth = int1 * int2
    print("What is", int1, '*', int2, '?')
    global userans
    userans = int(input())


def mysubtract():
    int1 = random.randint(1, 100)
    int2 = random.randint(1, 100)
    global groundtruth
    groundtruth = int1 - int2
    print('What is', int1, '-', int2, '?')
    global userans
    userans = int(input())


def sqrtint():
    int1 = random.randint(100, 10000)
    global groundtruth
    groundtruth = round(math.sqrt(int1), 0)
    print('What integer is closest to the square root of', int1, '?')
    global userans
    userans = int(input())


def unitdig():
    int1 = random.randint(1, 9)
    int2 = random.randint(2, 100)
    global groundtruth
    groundtruth = (int1**int2) % 10
    print('What is the unit value of', int1, '^', int2, '?')
    global userans
    userans = int(input())


questionlist = [
    myadder,
    mysubtract,
    sqrtint,
    mymultiple,
    unitdig
]

try:
    qnum = int(input('How many questions? \n'))
    currentscore = 0
except:
    print('I\'m sorry, I don\'t recognise that as a number.')

try:
    for i in range(1, qnum+1):
        random.choice(questionlist)()
        answerer()
    print('You scored', score, 'out of', qnum)
except:
    pass
