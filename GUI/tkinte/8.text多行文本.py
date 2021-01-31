# coding:utf-8
from tkinter import *
import webbrowser


class Application(Frame):
    """一个经典的GUI程序类写法"""
    def __init__(self, master=None):
        super().__init__(master)          # super代表的是父类的定义,而不是父类的对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建登录界面组件"""
        self.w1 = Text(root, width=40, height=12, bg='white')
        self.w1.pack()
        self.w1.insert(1.0, '123456789\nabcdefg')
        self.w1.insert(2.3, 'ooooooooooooooooo')


        Button(self, text='重复插入文本', command=self.insertText).pack(side='left')
        Button(self, text='返回文本', command=self.returnText).pack(side='left')
        Button(self, text='插入图片', command=self.addImage).pack(side='left')
        Button(self, text='添加组件', command=self.addWidget).pack(side='left')
        Button(self, text='通过tag精确控制文本', command=self.testTag).pack(side='left')


    def insertText(self):
        # INSERT索引表示在光标处插入
        self.w1.insert(INSERT, 'Xujie')
        # END索引表示在最后插入
        self.w1.insert(END, 'Liran')
        self.w1.insert(1.2, 'Xujie')


    def returnText(self):
        # Indexes索引用来指向Text组件中文本配置, Text组件索引也是对应实际字符之间的位置
        #核心:行号从1开始, 列号从零开始
        print(self.w1.get(1.2, 1.6))
        print('所有文本内容\n'+self.w1.get(1.0, END))


    def addImage(self):
        self.photo = PhotoImage(file=r"../\image/\1.gif ")
        self.w1.image_create(END, image=self.photo)


    def addWidget(self):
        b1 = Button(self.w1, text='爱liran')
        # 在text组件中创建命令
        self.w1.window_create(INSERT, window=b1)


    def testTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, 'good good study, day04填充日期数字区域读取 day04填充日期数字区域读取 up!\n百度搜索')
        self.w1.tag_add('good', 1.0, 1.9)
        self.w1.tag_config('good', background='red',foreground='yellow')
        self.w1.tag_add('baidu', 2.0, 2.2)
        self.w1.tag_config('baidu', underline=True)
        self.w1.tag_bind('baidu', '<Button-1>', self.webshow)


    def webshow(self, event):
        webbrowser.open('http://www.baidu.com')



if __name__ == "__main__":
    root = Tk()
    root.geometry("400x450+200+300")
    root.title('测试')
    app = Application(master=root)
    root.mainloop()