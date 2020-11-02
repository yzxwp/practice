#coding: utf-8
from tkinter import *

root = Tk()
root.geometry('500x300')

f1 = Frame(root, width=200, height=200, bg='gray')
f1.place(x=30, y=30)

Button(root, text='Xujie').place(relx=0.2, x=100, y=20, relwidth=0.2, relheight=0.5)
Button(f1, text='Liran').place(relx=0.6, rely=0.4)


root.mainloop()