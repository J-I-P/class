import pandas as pd

datas = [[65, 92, 78, 83, 70], [90, 72, 76, 93, 56], [81, 85, 91, 89, 77], [79, 53, 47, 94, 80]]
indexs = ["林小明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文","數學","英文","自然","社會"]

df = pd.DataFrame(datas, index=indexs, columns=columns)
print(df)

df1 = df.sort_values(by="數學", ascending=False)
print(df1)

df2 = df.sort_values(by="數學", ascending=True)
print(df2)

df3 = df.sort_index(axis=0, ascending=False) # 列
print(df3)

df4 = df.sort_index(axis=1, ascending=False) # 行
print(df4)