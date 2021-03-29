import pandas as pd
import numpy as np


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../day09_图形的生产/demo/023/Orders.xlsx", engine="openpyxl")

    pf["Year"] = pd.DatetimeIndex(pf["Date"]).year
    print(pf.head())
    # pt1 = pf.pivot_table(index="Category", columns="Year", values="Total", aggfunc=np.sum)
    # print(pt1)

    groups = pf.groupby(["Category", "Year"])
    s = groups["Total"].sum()
    c = groups["ID"].count()

    pt2 = pd.DataFrame({"Sum": s, "Count": c})
    print(pt2)


if __name__ == '__main__':
    way()
