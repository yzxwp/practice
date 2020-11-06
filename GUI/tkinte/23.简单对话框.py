# coding:utf-8
from tkinter import *
from tkinter.simpledialog import *

root = Tk()
root.geometry('530x200')


def text01():
    a = askinteger(title='年龄', prompt='请输入年龄', initialvalue=18, minvalue=1, maxvalue=150)
    show['text'] = a


Button(root, text='Xujie有多大?', command=text01).pack()
show = Label(root, width=40, height=3, bg='light pink')
show.pack()


root.mainloop()