# encoding:utf-8
import pandas as pd
import demjson


def way():
    # 从第几行开始读，从第0行开始，
    # 使用场景：例如第一行有脏数据
    data = pd.read_csv(r"./1.csv", encoding="gbk", header=1)
    # shape告诉我们有多少行多少列
    print(data.shape)
    # 查看有列
    print(data.columns)
    # 查看前几条数据
    print(data.head(7))
    # 查看末尾几行
    print(data.tail(3))
    # data2 = pd.read_csv(r"./2.csv", encoding="gbk")
    # print(data2)


if __name__ == '__main__':
    way()
