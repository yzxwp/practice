import pandas as pd
from matplotlib import pyplot as p


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("./demo/014/home_data.xlsx", engine="openpyxl")
    #相关性
    print(pf.corr())



if __name__ == '__main__':
    way()
