import pandas as pd


def Age_18_to_30(a):
    return 18 <= a <= 30


def leve_a(s):
    return 80 <= s


def way():
    pf = pd.read_excel("./1.xlsx", engine="openpyxl", index_col='ID')
    # pf = pf.loc[pf['Age'].apply(Age_18_to_30)].loc[pf['Score'].apply(leve_a)]
    # pf = pf.loc[pf.Age.apply(Age_18_to_30)].loc[pf.Score.apply(leve_a)]
    pf = pf.loc[pf.Age.apply(lambda x: 18 <= x <= 30)] \
        .loc[pf.Score.apply(lambda x: 80 <= x)]
    print(pf)


if __name__ == '__main__':
    way()
