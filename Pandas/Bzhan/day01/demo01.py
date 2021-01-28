# encoding:utf-8
import pandas as pd


def way():
    df = pd.DataFrame()
    df.to_excel("./demo.xlsx")
    print("OK")


if __name__ == '__main__':
    way()
