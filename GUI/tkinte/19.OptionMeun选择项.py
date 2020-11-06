# coding:utf-8
from tkinter import *
root = Tk()
root.geometry('530x300')


v = StringVar(root)
v.set('Xujie')
om = OptionMenu(root, v, 'liran', 'Xujie', 'linfeng', 'Anne')
om['width'] = 10
om.pack()


def test01():
    print('最喜欢的人', v.get())

Button(root, text='确定', command=test01).pack()

root.mainloop()
