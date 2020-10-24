#encoding:utf-8
# author:闫振兴
# contact: 1753502691@qq.com
# datetime:2020/10/20 20:31
# software: PyCharm
"""
文件说明：
"""
import pandas

if __name__ == '__main__':
    filename=r'./测试数据.csv'
    data=pandas.read_csv(filename, header=1 , encoding='GBK')
    # print(data)
    # 输出某一列的数据，注意当header！=0的时候无法使用
    # print(data['领域'])
    # 获得表的维度
    print(data.shape)
