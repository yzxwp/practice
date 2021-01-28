import pandas as pd


def way():
    s1 = pd.Series([1, 2, 3, 4], index=[1, 2, 3, 4], name="A")
    s2 = pd.Series([10, 20, 30, 40], index=[1, 2, 3, 4], name="B")
    s3 = pd.Series([100, 200, 300, 400], index=[1, 2, 3, 4], name="C")
    df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
    df2 = pd.DataFrame({"AA": s1, "BB": s2, "CC": s3})
    print(df)
    print(df2)


def way2():
    s1 = pd.Series([1, 2, 3, 4], index=[1, 2, 3, 4], name="A")
    s2 = pd.Series([10, 20, 30, 40], index=[1, 2, 3, 4], name="B")
    s3 = pd.Series([100, 200, 300, 400], index=[1, 2, 3, 4], name="C")
    df = pd.DataFrame([s1, s2, s3])
    print(df)


if __name__ == '__main__':
    way2()
