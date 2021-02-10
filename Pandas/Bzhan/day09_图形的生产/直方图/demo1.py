import pandas as pd
from matplotlib import pyplot as p


def way():
    pd.options.display.max_columns = 111
    pf = pd.read_excel("../demo/014/home_data.xlsx", engine="openpyxl")
    print(pf.head())
    # pf.plot.scatter(x='sqft_living', y='price')
    # pf.sqft_living.plot.hist(bins=1000)
    # p.xticks(range(0, max(pf.sqft_living), 500), fontsize=8, rotation=90)
    pf.price.plot.hist(bins=1000)
    p.xticks(range(0, max(pf.price), 100000), fontsize=8, rotation=90)
    p.show()


if __name__ == '__main__':
    way()
