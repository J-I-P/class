import pandas as pd

datas = [[65, 92, 78, 83, 70], [90, 72, 76, 93, 56], [81, 85, 91, 89, 77], [79, 53, 47, 94, 80]]
indexs = ["林小明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文","數學","英文","自然","社會"]

df = pd.DataFrame(datas, index=indexs, columns=columns)

df1 = df.drop("陳聰明")
print(df1)

df2 = df.drop("數學", axis=1)
print(df2)

df3 = df.drop(["數學", "自然"], axis=1)
print(df3)

df4 = df.drop(df.index[1:4], axis=0)
print(df4)

df5 = df.drop(df.columns[1:4], axis=1)
print(df5)
print(df5.ix[1:3, :])
print(df5.ix[1:3, 1])