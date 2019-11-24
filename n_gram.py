# -*- coding: utf-8 -*-

import sys
import pandas as pd
from infrastructure.mydict import MyDict

#　n-gram的n值
n = int(sys.argv[1])
# n = 3
print("n = ", n)

origin = pd.read_csv("data.csv")
mdict = MyDict()
feature = origin["Feature"].str.split("|")
total = len(feature)
for i, code in enumerate(feature):
    mdict.newLayer()
    if not type(code) == list:
        continue
    for method in code:
        length = len(method)
        if length < n:
            continue
        for start in range(length - (n - 1)):
            end = start + n
            mdict.mark(method[start:end])
    print("已完成", i+1, "个应用")
    print("百分比为：",(i + 1) * 100 / total, "%")

result = mdict.dict
result['isMalware']=origin.isMalware
pd.DataFrame(result, index=origin.index)\
               .to_csv("./" + str(n) + "_gram.csv", index=False)
