# coding:utf-8
from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):
    """一个经典的GUI程序类写法"""
    def __init__(self, master=None):
        super().__init__(master)          # super代表的是父类的定义,而不是父类的对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas = Canvas(self, width=200, height=300, bg='skyblue')
        self.canvas.pack()
        # 画一条直线
        line = self.canvas.create_line(10, 10, 20, 70, 70, 70)
        # 画一个矩形
        rect = self.canvas.create_rectangle(50, 50, 70, 70)
        # 画一个椭圆
        oval = self.canvas.create_oval(50, 50, 70, 70)

        Button(self, text='画十个矩形', command=self.drew).pack(side='left')

    def drew(self):
        for i in range(0, 10):
            x1 = random.randrange(int(self.canvas['width'])/2)
            y1 = random.randrange(int(self.canvas['height'])/2)
            x2 = x1 + random.randrange(int(self.canvas['width'])/2)
            y2 = y1 + random.randrange(int(self.canvas['height'])/2)
            self.canvas.create_rectangle(x1, y1, x2, y2)


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x350+200+300")
    root.title('canvas')
    app = Application(master=root)
    root.mainloop()