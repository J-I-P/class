import pandas as pd

table = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/AQI/?$format=csv")

table = table.drop(table.columns[12:], axis=1)
table = table.drop(table.columns[2:11], axis=1)
table = pd.DataFrame(table)
table = table.sort_values(by="PM2.5")

table.index = range(len(table))

print(table.head(3))
print(table)
