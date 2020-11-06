# coding:utf-8
from tkinter import *
root = Tk()
root.geometry('530x200')


def text01(value):
    print('滑块的值:', value)
    newFont = ('黑体', value)
    a.config(font=newFont)


s1 = Scale(root, from_=10, to=50, length=200, tickinterval=5, orient=HORIZONTAL, command=text01)
s1.pack()
a = Label(root, text='Xujie', width=10, height=1, bg='pink', fg='blue')
a.pack()
root.mainloop()