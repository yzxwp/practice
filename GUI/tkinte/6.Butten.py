# coding:utf-8
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """一个经典的GUI程序类写法"""

    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义,而不是父类的对象
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(root, text='登录', command=self.login,width=16,height=4,anchor=NE )
        self.btn01.pack()
        global photo
        photo = PhotoImage(file=r"../\image/\1.gif ")
        self.btn02 = Button(root, image=photo, command=self.login, state=DISABLED)
        self.btn02.pack()

    def login(self):
        messagebox.showinfo('命名系统', '生产一个身份证号码')


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x450+200+300")
    root.title('测试')
    app = Application(master=root)
    root.mainloop()
