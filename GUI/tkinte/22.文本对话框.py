# coding:utf-8
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry('530x200')


def text01():
    with askopenfile(title='上传文件', initialdir='e:', filetypes=[('可读文件', '.txt')])as f:
        show['text'] = f.read()

Button(root, text='选择读取的文本', command=text01).pack()
show = Label(root, width=40, height=3, bg='light pink')
show.pack()


root.mainloop()