# encoding:utf-8

import pandas as pd
from matplotlib import pyplot as p
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 设置matplotlib可以显示汉语
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 16


def way():
    pf = pd.read_excel("./11.xlsx", engine="openpyxl")
    pf.sort_values(by='Score2', inplace=True, ascending=False)
    print(pf)
    # pf.plot.bar(x='Name', y=['Score1', 'Score2'], color=['orange', 'red'], title=u"title name")
    pf.plot.bar(x='Name', y=['Score1', 'Score2'], color=['orange', 'red'])
    p.title("图片 name")
    p.xlabel("产品名称", fontweight='bold')
    p.ylabel("销量", fontweight='bold')
    ax = p.gca()
    ax.set_xticklabels(pf['Name'], rotation=45, ha='right')
    p.tight_layout()
    f = p.gcf()
    f.subplots_adjust(left=0.1,bottom=0.2)
    p.show()


if __name__ == '__main__':
    way()
