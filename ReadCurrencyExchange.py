import pandas as pd
tables = pd.read_html("http://www.stockq.org/market/currency.php")
print(tables[7])
x=len(tables)
#print(x)
table = tables[x-3]
#print(table)
table = table.drop(table.index[0:1])
#table = table.drop(table.columns[0:1],axis=1)
#table = table.drop(table.columns[3:5],axis=1)
#print(table.head(12))