import pandas as pd

datas = [[65, 92, 78, 83, 70], [90, 72, 76, 93, 56], [81, 85, 91, 89, 77], [79, 53, 47, 94, 80]]
indexs = ["林小明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文","數學","英文","自然","社會"]

df = pd.DataFrame(datas, index=indexs, columns=columns)

print(df.loc["陳聰明", :])
print(df.loc[:, "英文"])

print(df.loc["陳聰明"]["數學"])

print(df.loc[("陳聰明", "熊小娟"), :])

print(df.loc[:, ("數學", "自然")])

print(df.loc[("陳聰明", "熊小娟"), ("數學", "自然")])

print(df.loc["陳聰明":"熊小娟", "數學":"自然"])

print(df.loc[:"黃美麗", "數學":"自然"])

print(df.loc["陳聰明":, "數學":"自然"])