import random
import math
# import tkinter as tk
# from tkinter import simpledialog
# root = tk.Tk()
# greeting = tk.Label(text="Hello, Tkinter")
# root.mainloop()
# def sqrtint(bigint):
#    userans = int(input('What integer is closest to the square root of', bigint))
#    if userans == bigint:
#        print('True!')

groundtruth = 0
userans = 0
qnum = 0
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

