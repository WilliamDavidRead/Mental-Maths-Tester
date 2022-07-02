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

#def answerer():
#    try:
#        userans = int(input())
#        if userans == groundtruth:
#            print('Correct')
#        else:
#            print('Incorrect, the correct answer is', groundtruth)
#    except:
#        print('I\'m sorry I didn\'t understand that, please answer using integers.')

def myadder():
    int1 = random.randint(1, 100)
    int2 = random.randint(1, 100)
    groundtruth = int1 + int2
    print("What is", int1, '+', int2, '?')
    userans = int(input())
    if userans == groundtruth:
        print('Correct')
    else:
        print('Incorrect, the correct answer was', groundtruth)


def mymultiple():
    int1 = random.randint(1, 100)
    int2 = random.randint(1, 100)
    groundtruth = int1 * int2
    print("What is", int1, '*', int2, '?')
    userans = int(input())
    if userans == groundtruth:
        print('Correct')
    else:
        print('Incorrect, the correct answer was', groundtruth)


def mysubtract():
    int1 = random.randint(1, 100)
    int2 = random.randint(1, 100)
    groundtruth = int1 - int2
    print('What is', int1, '-', int2, '?')
    userans = int(input())
    if userans == groundtruth:
        print('Correct')
    else:
        print('Incorrect, the correct answer was', groundtruth)


def sqrtint():
    int1 = random.randint(100, 10000)
    groundtruth = round(math.sqrt(int1), 0)
    print('What integer is closest to the square root of', int1, '?')
    userans = int(input())
    if userans == groundtruth:
        print('Correct')
    else:
        print('Incorrect, the correct answer was', groundtruth)


def unitdig():
    int1 = random.randint(1, 9)
    int2 = random.randint(2, 100)
    groundtruth = (int1**int2) % 10
    print('What is the unit value of', int1, '^', int2, '?')
    userans = int(input())
    if userans == groundtruth:
        print('Correct')
    else:
        print('Incorrect, the correct answer was', groundtruth)


questionlist = [
#    myadder,
#    mysubtract,
#    sqrtint,
#    mymultiple,
    unitdig
]

try:
    qnum = int(input('How many questions? \n'))
except:
    print('I\'m sorry, I don\'t recognise that as a number.')

try:
    for i in range(1, qnum+1):
        random.choice(questionlist)()
    print('That\'s all, folks')
except:
    pass