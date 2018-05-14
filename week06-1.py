import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
tables = pd.read_html("https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.99842400%201523326567")
x=len(tables)
table = tables[x-2]
table = table.drop(table.columns[0:1], axis=1)
table = table.drop(table.columns[3:5], axis=1)
table = table.drop(table.columns[4:7], axis=1)

i = 0
for data in (table[6]):
    if data[0]!='△' and i>0:
        table = table.drop(table.index[i])
        i-=1
    i+=1
print(table)