import pandas as pd


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_csv("../day09_图形的生产/demo/022/Students.csv", index_col="ID")
    print(pf)

    pf2 = pd.read_csv("../day09_图形的生产/demo/022/Students.tsv", sep='\t', index_col="ID")
    print(pf2)

    pf3 = pd.read_csv("../day09_图形的生产/demo/022/Students.txt", sep='|', index_col="ID")
    print(pf3)


if __name__ == '__main__':
    way()
