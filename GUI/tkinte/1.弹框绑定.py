from tkinter import *
from tkinter import messagebox

root = Tk()
btn01 = Button(root)
btn01["text"] = "获得一个身份证号码"
btn01.pack()


def way():
    return '1221211212'


def get_car(e):
    messagebox.showinfo("身份证号码", way())
    print("1111")


# 调用组件的mainloop()方法，进入事件循环
btn01.bind("<Button-1>", get_car)
root.mainloop()
