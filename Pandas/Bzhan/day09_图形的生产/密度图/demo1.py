import pandas as pd
from matplotlib import pyplot as p


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../demo/014/home_data.xlsx", engine="openpyxl")
    print(pf.head())
    pf.sqft_living.plot.kde()
    p.xticks(range(0, max(pf.sqft_living), 500), fontsize=8, rotation=90)
    p.show()


if __name__ == '__main__':
    way()
