# encoding:utf-8
import pandas as pd

dict = {"name": [u"张三", u"李四", u"王五", u"鸺鹠", u"枸杞", u"篱笆", u"实权"],
        "sex": ["S", "M", "S", "S", "S", "M", "M"],
        "class": [u"一班", u"二班", u"一班", u"二班", u"一班", u"二班", u"一班"]}
data = pd.Series(dict)
print(data)
print(data.index)
print(data.values)
print(data.value_counts("name"))
