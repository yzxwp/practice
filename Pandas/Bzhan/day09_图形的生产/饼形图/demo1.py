#encoding:utf-8
import pandas as pd
from matplotlib import pyplot as p
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 设置matplotlib可以显示汉语
mpl.rcParams['axes.unicode_minus'] = False
mpl.rcParams['font.size'] = 16

def way():
    pf=pd.read_excel('./1.xlsx',engine='openpyxl',index_col="USER")
    print(pf)
    # pf["Chinese"].sort_values(ascending=True).plot.pie(fontsize=16,startangle=-270)
    pf["Chinese"].plot.pie(fontsize=16, counterclock=False)
    p.title("饼形图标题")
    p.ylabel("USER",fontsize=26,fontweight='bold')
    p.show()

if __name__ == '__main__':
    way()