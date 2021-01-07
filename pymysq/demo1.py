#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql


def way():
    # 连接数据库
    # conn = pymysql.connect('rm-uf6509356w9nq5x41vo.mysql.rds.aliyuncs.com', 'yzxing', 'YAN123@@@')

    # 也可以使用关键字参数
    conn = pymysql.connect(host='rm-uf6509356w9nq5x41vo.mysql.rds.aliyuncs.com', port=3306, user='yzxing',
                           passwd='YAN123@@@', db='web_member', charset='utf8')

    sql = "select * from table"

    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()
    print("链接成功")
    # 因该模块底层其实是调用CAPI的，所以，需要先得到当前指向数据库的指针。
    # 关闭游标连接
    # cursor.close()
    # 关闭数据库连接
    # conn.close()


if __name__ == '__main__':
    way()
