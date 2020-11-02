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
        """创建登录界面组件"""
        self.lable01=Label(self,text='用户名：')
        self.lable01.pack()
        #StringVar 变量绑定到指定的组件
        #StringVar发生变化，StringVar的值也发生变化
        value01=StringVar()
        self.entry01=Entry(self,textvariable=value01)
        self.entry01.pack()
        value01.set("admin")
        print(value01.get())
        print(self.entry01.get())

        self.lable02 = Label(self, text='密码：')
        self.lable02.pack()
        value02 = StringVar()
        self.entry02 = Entry(self, textvariable=value02 ,show="*")
        self.entry02.pack()
        # value02.set("123")
        # print(value02.get())
        # print(self.entry02.get())



        Button(self,text="登录",command=self.login).pack()

    def login(self):
        username=self.entry01.get()
        pwd=self.entry02.get()
        if username!='admin':
            messagebox.showinfo(title='信息',message="用户名错误")
        if pwd!="111":
            messagebox.showinfo(title='信息',message="密码错误")
        if username == 'admin'and pwd=="111":
            data = "用户名：" + self.entry01.get() + "   密码：" + self.entry02.get()
            messagebox.showinfo(title='信息',message=data)



    #   居中显示方法
    def center_window(root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        print(size)
        root.geometry(size)
        root.update()
        print(root.winfo_x())


if __name__ == "__main__":
    root = Tk()
    root.title('测试')
    Application.center_window(root,600,400)
    app = Application(master=root)
    root.mainloop()
