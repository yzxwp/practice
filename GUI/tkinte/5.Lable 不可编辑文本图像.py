# encoding:utf8
from tkinter import *
from tkinter import Label
import random
import time


class Application(Frame):
    """
        经典的面向对象GUI写法
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        # 文字
        self.lable01 = Label(self, text='Lable呀', width=10, height='2', bg='white', fg='black')
        self.lable01.pack()
        # 图片
        global photo
        photo = PhotoImage(file=r"../\image/\1.gif ")
        self.lable02 = Label(self, image=photo)
        self.lable02.pack()

        # 多行文本
        self.lable03 = Label(self, text="身\n份\n证\n号\n码", borderwidth=1, relief="solid", justify="right")
        self.lable03.pack()

    #   居中显示方法
    def center_window(root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        print(size)
        root.geometry(size)
        root.update()


root = Tk()
root.title('一个经典的GUI程序类')
Application.center_window(root, 1000, 700)
app = Application(master=root)
root.mainloop()
