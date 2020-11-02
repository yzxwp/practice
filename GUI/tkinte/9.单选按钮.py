# coding:utf-8
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序类写法"""
    def __init__(self, master=None):
        super().__init__(master)          # super代表的是父类的定义,而不是父类的对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.v = StringVar()
        self.v.set("M")

        self.r1 = Radiobutton(self, text='Xujie', value='M', variable=self.v)
        self.r2 = Radiobutton(self, text='Liran', value='W', variable=self.v)
        self.r1.pack(side='left')
        self.r2.pack(side='left')
        Button(self, text='确定', command=self.confirm).pack(side='left')

    def confirm(self):
        messagebox.showinfo('测试', '选择主角:'+self.v.get())



if __name__ == "__main__":
    root = Tk()
    root.geometry("400x450+200+300")
    root.title('测试')
    app = Application(master=root)
    root.mainloop()