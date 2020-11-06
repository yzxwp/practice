# coding:utf-8
from tkinter import *
root = Tk()
root.geometry('530x300')

c1 = Canvas(width=200, height=200, bg='green')
c1.pack()


def mouseTest(event):
    print('鼠标左键单击位置(相对于父容器):{0},{1}'.format(event.x, event.y))
    print('鼠标左键单击位置(相对于屏幕):{0},{1}'.format(event.x_root, event.y_root))
    print('事件绑定的组件:{0}'.format(event.widget))


def TestDrag(event):
    c1.create_oval(event.x, event.y, event.x+1, event.y+1)


def keyboardTest(event):
    print('键的keycode:{0}, 键的char:{1}, 键的keysym:{2}'.format(event.keycode, event.char, event.keysym))


def press_a_Test(event):
    print('press a')


def release_a_Test(event):
    print('release a')


c1.bind('<Button-1>', mouseTest)
c1.bind('<B1-Motion>', TestDrag)
root.bind('<KeyPress>', keyboardTest)
root.bind('<KeyPress-a>', press_a_Test)
root.bind('KeyRelease-a', release_a_Test)

root.mainloop()