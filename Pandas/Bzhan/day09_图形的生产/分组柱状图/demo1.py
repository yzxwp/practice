# encoding:utf-8

import pandas as pd


def way():
    pf = pd.read_excel("./1.xlsx", engine="openpxyl")
    print(pf)


if __name__ == '__main__':
    way()