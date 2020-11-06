# -*- coding:utf-8 -*-
from tkinter import *
import GUI.tk_practice.demo_way as dd
import 随机获得身份证号码 as id_card
import 随机生成统一社会征信码 as id_credit
import 随机生成电话号码 as phone
import 随机获得姓名 as name
import 随机获得车架号VIN as vin
import 随机获得银行卡号 as bank_card


class demo():
    def __init__(self):
        self.root = Tk()
        self.root.title("自动生成测试数据小工具")  # 设置窗口标题
        dd.center_window(self.root, 350, 270)
        self.way()

    def way(self):
        # 用户姓名
        self.lab_name = Label(self.root, text='用 户  姓 名 ：').grid(row=0, column=1)
        self.text_name = Text(self.root, height=1, width=20)
        self.text_name.insert('0.0', name.random_name())
        self.text_name.grid(row=0, column=2, sticky=W)
        self.text_name_click = Button(self.root, text='重新获取：',command=self.text_name1).grid(row=0, column=3, sticky=W)

        # 手机号码
        self.lab_phone = Label(self.root, text='手 机  号 码 ：').grid(row=1, column=1)
        self.text_phone = Text(self.root, height=1, width=20)
        self.text_phone.insert('0.0', phone.phone_num())
        self.text_phone.grid(row=1, column=2, sticky=W)
        self.text_phone_click = Button(self.root, text='重新获取：',command=self.text_phone1).grid(row=1, column=3, sticky=W)

        # 身份证号码
        self.lab_idcard = Label(self.root, text='身 份 证 号 码 ：').grid(row=2, column=1)
        self.text_idcard = Text(self.root, height=1, width=20)
        self.text_idcard.insert('0.0', id_card.main())
        self.text_idcard.grid(row=2, column=2, sticky=W)
        self.text_idcard_click = Button(self.root, text='重新获取：',command=self.text_idcard1).grid(row=2, column=3, sticky=W)

        # 统一社会征信码
        self.lab_tyshzxm = Label(self.root, text='统一社会征信码：').grid(row=3, column=1)
        self.text_tyshzxm = Text(self.root, height=1, width=20)
        self.text_tyshzxm.insert('0.0', id_credit.create_social_credit())
        self.text_tyshzxm.grid(row=3, column=2, sticky=W)
        self.text_tyshzxm_click = Button(self.root, text='重新获取：',command=self.text_tyshzxm1).grid(row=3, column=3, sticky=W)

        # 组织机构代码
        self.lab_zzjgdm = Label(self.root, text='组织 机构 代码：').grid(row=4, column=1)
        self.text_zzjgdm = Text(self.root, height=1, width=20)
        self.text_zzjgdm.insert('0.0', id_credit.create_organization())
        self.text_zzjgdm.grid(row=4, column=2, sticky=W)
        self.text_zzjgdm_click = Button(self.root, text='重新获取：',command=self.text_zzjgdm1).grid(row=4, column=3, sticky=W)

        #随机获得车架号
        self.lab_vin = Label(self.root, text='车辆 车架 号：').grid(row=5, column=1)
        self.text_vin = Text(self.root, height=1, width=20)
        self.text_vin.insert('0.0', vin.random_vin())
        self.text_vin.grid(row=5, column=2, sticky=W)
        self.text_vin_click = Button(self.root, text='重新获取：',command=self.text_vin1).grid(row=5, column=3, sticky=W)

        # 随机获得工行银行卡
        self.lab_bank_gon = Label(self.root, text='工行 银行卡号：').grid(row=6, column=1)
        self.text_bank_gon = Text(self.root, height=1, width=20)
        self.text_bank_gon.insert('0.0', bank_card.gen_bank_card_nonghang())
        self.text_bank_gon.grid(row=6, column=2, sticky=W)
        self.text_bank_gon_click = Button(self.root, text='重新获取：',command=self.text_bank_gon1).grid(row=6, column=3, sticky=W)

        # 随机获得农行银行卡
        self.lab_bank_non = Label(self.root, text='农行 银行卡号：').grid(row=7, column=1)
        self.text_bank_non = Text(self.root, height=1, width=20)
        self.text_bank_non.insert('0.0', bank_card.gen_bank_card_gonghang())
        self.text_bank_non.grid(row=7, column=2, sticky=W)
        self.text_bank_non_click = Button(self.root, text='重新获取：',command=self.text_bank_non1).grid(row=7, column=3, sticky=W)

        self.root.mainloop()

    def text_name1(self):
        self.text_name.delete('0.0', END)
        self.text_name.insert('0.0', name.random_name())

    def text_phone1(self):
        self.text_phone.delete('0.0', END)
        self.text_phone.insert('0.0', phone.phone_num())

    def text_idcard1(self):
        self.text_idcard.delete('0.0', END)
        self.text_idcard.insert('0.0',id_card.main())

    def  text_tyshzxm1(self):
        self.text_tyshzxm.delete('0.0', END)
        self.text_tyshzxm.insert('0.0', id_credit.create_social_credit())

    def text_zzjgdm1(self):
        self.text_zzjgdm.delete('0.0', END)
        self.text_zzjgdm.insert('0.0', id_credit.create_organization())

    def text_vin1(self):
        self.text_vin.delete('0.0', END)
        self.text_vin.insert('0.0', vin.random_vin())

    def text_bank_gon1(self):
        self.text_bank_gon.delete('0.0', END)
        self.text_bank_gon.insert('0.0', bank_card.gen_bank_card_gonghang())

    def text_bank_non1(self):
        self.text_bank_non.delete('0.0', END)
        self.text_bank_non.insert('0.0', bank_card.gen_bank_card_nonghang())

if __name__ == '__main__':
    demo()
