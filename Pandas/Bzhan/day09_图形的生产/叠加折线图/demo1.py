# encoding:utf-8
import pandas as pd
from matplotlib import pyplot as p
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 设置matplotlib可以显示汉语
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 16


def way():
    pf = pd.read_excel('./1.xlsx', engine='openpyxl', index_col="USER")
    print(pf)
    print(pf.columns)
    pf.plot(y=['Chinese', 'English', 'Janpan'])
    p.title(u"zhexiantu", fontsize=18)
    p.ylabel(u"hengji", fontsize=18)
    p.xlabel("yonghumingcheng", fontsize=18)
    p.xticks(pf.ID, fontsize=8)
    p.show()


if __name__ == '__main__':
    way()
