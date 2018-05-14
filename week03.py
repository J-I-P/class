import pandas as pd
from pandas import ExcelWriter

data = pd.read_csv('105_XiTun.csv', encoding='big5')

def solError(tmp):
    if "nan" == str(tmp):
        return float(0.0)
    if "x" in str(tmp) or "#" in str(tmp):
        #tmp1 = tmp.replace("x", "")
        tmp1 = tmp.rstrip('x#')
        return float(tmp1)
    #if "#" in str(tmp):
     #   tmp1 = tmp.replace("#", "")
      #  return float(tmp1)
    return float(tmp)

#print(df.iloc[2][12][1])
#print(data.iloc[:,12])
#print(data)

dayOfMonth = [-1,0,0,0,0,0,0,0,0,0,0,0,0]
for row in data['日期']:
    tmp = row.split('/')
    dayOfMonth[int(tmp[1])] += 1

index = 0
for i in dayOfMonth:
     dayOfMonth[index] = int(int(i) / 20)
     index += 1

#print(dayOfMonth)

cosum = pmsum = so2sum = 0.0
costart = int(2)
pmstart = int(10)
so2start = int(14)
co = []
pm = []
so2 = []

for i in range(1,13):
    cosum = pmsum = so2sum = 0

    for day in range(dayOfMonth[i]):
        cosum += solError(data.iloc[costart][12])
        pmsum += solError(data.iloc[pmstart][12])
        so2sum += solError(data.iloc[so2start][12])

        costart += 20
        pmstart += 20
        so2start += 20

    co.append(cosum / dayOfMonth[i])
    pm.append(pmsum / dayOfMonth[i])
    so2.append(so2sum / dayOfMonth[i])

#print(co)
#print(pm)
#print(so2)


datas = [pm, co, so2]
indexs = ["PM2.5", "CO", "SO2"]
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
df = df.T

print(df)

writer = ExcelWriter('XiTun_Analysis.xlsx')
df.to_excel(writer,'Sheet2')
workbook = writer.book
worksheet = writer.sheets['Sheet2']
worksheet.conditional_format('A2:D13', {'type': '3_color_scale'})
#畫折線圖
chart = workbook.add_chart({'type': 'line'})

chart.add_series({'name': '=Sheet2!$B$1','categories': '=Sheet2!$A$2:$A$13','values': '=Sheet2!$B$2:$B$13'})
chart.add_series({'name': '=Sheet2!$C$1','categories': '=Sheet2!$A$2:$A$13','values': '=Sheet2!$C$2:$C$13'})
chart.add_series({'name': '=Sheet2!$D$1','categories': '=Sheet2!$A$2:$A$13','values': '=Sheet2!$D$2:$D$13'})

chart.set_x_axis({'name': 'Month'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': True}})
chart.set_legend({'position': 'top'})
worksheet.insert_chart('G2: W20', chart)
writer.save()