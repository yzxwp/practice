# coding:utf-8
from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry('530x200')


def text01():
    s1 = askcolor(color='red', title='选择背景色')
    print(s1)
    root.config(bg=s1[1])


Button(root, text='选择背景色', command=text01).pack()

root.mainloop()