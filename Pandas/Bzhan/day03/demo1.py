# encoding:utf-8
import pandas as pd


def way():
    L1 = [100, 200, 300]
    L2 = ["x", "y", "z"]
    data = pd.Series(L1, index=L2)
    print(data)
    

if __name__ == '__main__':
    way()
