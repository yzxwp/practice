import pandas as pd
from matplotlib import pyplot as p


def way():
    pd.options.display.max_columns = 111
    pf = pd.read_excel("../demo/014/home_data.xlsx", engine="openpyxl")
    print(pf.head())
    pf.plot.scatter(x='sqft_living', y='price')
    p.show()


if __name__ == '__main__':
    way()
