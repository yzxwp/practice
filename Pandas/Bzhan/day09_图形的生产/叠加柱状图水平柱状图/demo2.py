# encoding:utf-8

import pandas as pd
from matplotlib import pyplot as p
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 设置matplotlib可以显示汉语
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 16


def way():
    pf = pd.read_excel("./1.xlsx", engine="openpyxl")
    pf['totle']=pf['Chinese']+pf['English']+pf['Janpan']
    pf.sort_values(by="totle",inplace=True,ascending=True)
    print(pf)
    pf.plot.barh(x='USER',y=['Chinese','English','Janpan'],stacked=True,title='图标标题')
    p.tight_layout()
    p.show()


if __name__ == '__main__':
    way()
