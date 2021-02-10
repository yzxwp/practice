import pandas as pd


def way():
    pd.options.display.max_columns = 777
    pf = pd.read_excel("../day09_图形的生产/demo/018/Employees.xlsx", engine="openpyxl")
    print(pf)
    df = pf["Full Name"].str.split(" ", n=2, expand=True)
    print(df)
    pf["Fiest Name"] = df[0]
    pf["Last Name"] = df[1].str.upper()
    print(pf)


if __name__ == '__main__':
    way()
