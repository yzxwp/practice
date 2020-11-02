#encoding:utf8
from tkinter import *
from tkinter import messagebox
import random
import time


class Application(Frame):
    """
        经典的面向对象GUI写法
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.but01 = Button(self)
        self.but01["text"] = '身份证号码'
        self.but01.pack()
        self.but01['command'] = self.main1
        # # """创建退出按钮"""
        self.but02 = Button(self, text='退出', command=self.destroy)
        self.but02.pack()

    def regiun(self):
        '''生成身份证前六位'''
        # 列表里面的都是一些地区的前六位号码
        first_list = ['362402', '362421', '362422', '362423', '362424', '362425', '362426', '362427', '362428',
                      '362429', '362430', '362432', '110100', '110101', '110102', '110103', '110104', '110105',
                      '110106', '110107', '110108', '110109', '110111']
        first = random.choice(first_list)
        return first

    def year(self):
        '''生成年份'''
        now = time.strftime('%Y')
        # 1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
        second = random.randint(1948, int(now) - 18)
        # print('随机生成的身份证人员年龄为：'+str(age))
        return second

    def month(self):
        '''生成月份'''
        three = random.randint(1, 12)
        # 月份小于10以下，前面加上0填充
        if three < 10:
            three = '0' + str(three)
            return three
        else:
            return three

    def day(self):
        '''生成日期'''
        four = random.randint(1, 31)
        # 日期小于10以下，前面加上0填充
        if four < 10:
            four = '0' + str(four)
            return four
        else:
            return four

    def randoms(self):
        '''生成身份证后四位'''
        # 后面序号低于相应位数，前面加上0填充
        five = random.randint(1, 9999)
        if five < 10:
            five = '000' + str(five)
            return five
        elif 10 < five < 100:
            five = '00' + str(five)
            return five
        elif 100 < five < 1000:
            five = '0' + str(five)
            return five
        else:
            return five

    def main1(self):
        first = self.regiun()
        second = self.year()
        three = self.month()
        four = self.day()
        last = self.randoms()
        IDcard = str(first) + str(second) + str(three) + str(four) + str(last)
        print('随机生成的身份证号码为：'+IDcard)
        messagebox.showinfo(IDcard)
        # return IDcard

    #   居中显示方法
    def center_window(root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        print(size)
        root.geometry(size)
        root.update()


root = Tk()
root.title('一个经典的GUI程序类')
Application.center_window(root, 1000, 700)
app = Application(master=root)
root.mainloop()
