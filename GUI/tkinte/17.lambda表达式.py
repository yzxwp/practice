# coding:utf-8
from tkinter import *
root = Tk()
root.geometry('530x300')


def mouseTest1():
    print('112233')


def mouseTest2(a, b):
    print('a={0}, b={1}'.format(a, b))


Button(root, text='command1', command=mouseTest1).pack(side='left')
Button(root, text='command2', command=lambda: mouseTest2('Xujie', 'Liran')).pack(side='left')


root.mainloop()