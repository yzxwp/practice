#encoding:utf-8
# author:闫振兴
# contact: 1753502691@qq.com
# datetime:2020/10/20 21:10
# software: PyCharm
"""
文件说明：
"""
import pandas as pd
import numpy as np
if __name__ == '__main__':

    df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
     "date":pd.date_range('20130102', periods=6),
      "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
     "age":[23,44,54,32,34,32],
     "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
      "price":[1200,np.nan,2133,5433,np.nan,4432]},
      columns =['id','date','city','category','age','price'])
    df.to_csv(r'./createCsv.csv',encoding='GBK')