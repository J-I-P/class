import pandas as pd

#data = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv")
table = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/AQI/?$format=csv")
table = table.drop(table.columns[3:], axis=1)

good=[]
soso=[]
bad=[]
#print(table)

i=0
for data in (table["AQI"]):
    #table.ix[:, 2]
    tmp = table.ix[i][0] + table.ix[i][1]
    if data<=50:
        good.append(tmp)
    elif data>100:
        bad.append(tmp)
    else:
        soso.append(tmp)
    i+=1
    if i==len(table["AQI"]):
        break;

print("good:")
print(good)
print("soso:")
print(soso)
print("bad:")
print(bad)