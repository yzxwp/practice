# encoding:utf-8
import pandas as pd
from matplotlib import pyplot


def way():
    pf = pd.read_excel("./1.xlsx", engine="openpyxl")
    print(pf)
    pf.sort_values(by='Score', inplace=True, ascending=False)
    # pf.plot.bar(x='Name', y="Score", color='orange', title=u"zhuzhaungtubiaoqian")
    pyplot.bar(pf.Name, pf.Score, color='orange')
    # 旋转90度显示
    pyplot.xticks(pf.Name, rotation='90')
    pyplot.xlabel("Name")
    pyplot.ylabel("Score")
    # pyplot.title(u"柱状图")
    pyplot.tight_layout()
    # 紧凑型布局
    # pyplot.tight_layout()
    pyplot.show()
    pf.to_excel('./2.xlsx')


if __name__ == '__main__':
    way()
