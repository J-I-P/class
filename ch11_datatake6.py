import pandas as pd

datas = [[65, 92, 78, 83, 70], [90, 72, 76, 93, 56], [81, 85, 91, 89, 77], [79, 53, 47, 94, 80]]
indexs = ["林小明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文","數學","英文","自然","社會"]

df = pd.DataFrame(datas, index=indexs, columns=columns)

print(df.head(2))
print(df.tail(3))
