# coding:utf-8
from tkinter import *
import 随机获得身份证号码 as idcard


class Application(Frame):
    """一个经典的GUI程序类写法"""

    def __init__(self, master=None):
        super().__init__(master)  # super代表的是父类的定义,而不是父类的对象
        self.master = master
        self.pack()
        self.createWidget()
        self.height_width_text = Text(root, height=1, width=15).pack()
        self.height_width_text.grid(row=0, column=1, sticky=W)

    def createWidget(self):
        """创建登录界面组件"""
        self.w1 = Text(root, width=15, height=1, bg='white')
        self.w1.pack()
        self.w1.insert(1.0, idcard.main())

        self.height_width_label = Label(root, text='身份证号码：').pack()

        # self.height_width_label.grid(row=0, column=0, sticky=E)

        Button(self, text='身份证号码', command=idcard.main()).pack(side='left')


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x450+200+300")
    root.title('测试')
    app = Application(master=root)
    root.mainloop()
