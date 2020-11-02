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
        self.man = IntVar()
        self.woman = IntVar()
        print(self.man.get())
        self.c1 = Checkbutton(self, text='Xujie', variable=self.man, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self, text='liran', variable=self.woman, onvalue=1, offvalue=0)
        self.c1.pack(side='left')
        self.c2.pack(side='left')
        Button(self, text='确定', command=self.confirm).pack(side='left')

    def confirm(self):
        if self.man.get() == 1 and self.woman.get() == 0:
            messagebox.showinfo('你究竟喜欢谁', '原来你喜欢我啊!')
        if self.woman.get() == 1 and self.man.get() == 0:
            messagebox.showinfo('你究竟喜欢谁', '你居然喜欢女的!')
        if self.woman.get() == 1 and self.man.get() == 1:
            messagebox.showinfo('你究竟喜欢谁', '说!你到底喜欢谁!')
        if self.man.get() == 0 and self.woman.get() == 0:
            messagebox.showinfo('你究竟喜欢谁', '爱会消失的,对吗?')



if __name__ == "__main__":
    root = Tk()
    root.geometry("400x450+200+300")
    root.title('你究竟喜欢谁?')
    app = Application(master=root)
    root.mainloop()