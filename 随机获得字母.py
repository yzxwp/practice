import string   # 导入string这个模块
import random

if __name__ == '__main__':
     # print(string.digits)  # 输出包含数字0~9的字符串
     # print(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串
     # print(string.ascii_lowercase)  # 包含所有小写字母的字符串
     # print(string.ascii_uppercase)  # 包含所有大写字母的字符串
     # r.randint(a, b), 生成一个随机的整数，a是下限，b是上限。下限必须小于上限
     rr=random.randint(1000000000, 9999999999)
     s = string.ascii_letters
     # 大写string.ascii_uppercase
     # 小写string.ascii_lowercase
     r = random.choice(s)+random.choice(s)+random.choice(s)+random.choice(s)
     print(rr)