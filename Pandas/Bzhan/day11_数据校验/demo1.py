import pandas as pd
from matplotlib import pyplot as p


def score_validation(row):
    try:
        assert 0 <= row.Score <= 100
    except:
        print(f"#{row.ID}\tstudents {row.Name} has an invalid score {row.Score}")


def score_validation(row):
    if not  0 <= row.Score <= 100:
        print(f"#{row.ID}\tstudents {row.Name} has an invalid score {row.Score}")


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../day09_图形的生产/demo/017/Students.xlsx", engine="openpyxl")
    print(pf)
    pf.apply(score_validation, axis=1)


if __name__ == '__main__':
    way()
