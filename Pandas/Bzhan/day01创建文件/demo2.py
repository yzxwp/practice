# encoding:utf-8
import pandas as pd


def way():
    df = pd.DataFrame({"ID": [1, 2, 3, 4],
                       "Name": ["张三", "李四", "王五", "鸺鹠"],
                       "成绩": [67, 78, 89, 91]})
    df.set_index("ID", inplace=True)
    # df.reset_index("ID")
    print(df)
    df.to_excel("./demo1.xlsx")
    print("OK")


if __name__ == '__main__':
    way()
