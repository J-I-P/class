#使用pandas套件讀寫excel檔案, ref:E_7_12.py
import pandas as pd
from pandas import ExcelWriter
#from pandas import DataFrame

df1=pd.read_csv('105_XiTun.csv', encoding='big5')

allData = []
dayOfMonth = [-1,0,0,0,0,0,0,0,0,0,0,0,0]
#print(df1['9'])
for row in df1['日期']:
    tmp = row.split('/')
    #print(tmp[1])
    dayOfMonth[int(tmp[1])] += 1

index = 0
for i in dayOfMonth:
     dayOfMonth[index] = int(int(i) / 20)
     index += 1

print(dayOfMonth)

tmpInt = 0
for i in dayOfMonth:
    tmpInt += i

print(tmpInt) # total day in year

for row in df1['9']:
    # if row[0] == "PM2.5":
    #     print(row[1])
    allData.append(row)
#print(df1)
# each 20 per day indexAt(0~19)
# co no 3
# pm 2.5 11
# so2 15
all_co = []
all_pm = []
all_so2 = []
for idx, val in enumerate(allData):
    if idx % 20 == 2:
        all_co.append(val)
    if idx % 20 == 10:
        all_pm.append(val)
    if idx % 20 == 14:
        all_so2.append(val)
    #print(idx, val)



def solError(tmp):
    if "nan" == str(tmp):
        return float(0.0)
    if "x" in str(tmp):
        tmp1 = tmp.replace("x", "")
        return float(tmp1)
    if "#" in str(tmp):
        tmp1 = tmp.replace("#", "")
        return float(tmp1)
    return float(tmp)

allDayByTmp = []
allDayByTmp1 = []
allDayByTmp2 = []
totalIndex = 0
for i in dayOfMonth:
    getCount = i
    listTmp = []
    listTmp1 = []
    listTmp2 = []
    for k in range(getCount):
        listTmp.append(solError(all_co[totalIndex+k]))
        listTmp1.append(solError(all_pm[totalIndex+k]))
        listTmp2.append(solError(all_so2[totalIndex+k]))
    totalIndex += getCount
    allDayByTmp.append(listTmp)
    allDayByTmp1.append(listTmp1)
    allDayByTmp2.append(listTmp2)

#print(allDayByTmp)
#print(allDayByTmp1)
#print(allDayByTmp2)
#print(len(all_co))
#print(len(all_pm))
#print(len(all_so2))

#print(allData)

for i in range(1, 13):
    print(sum(allDayByTmp[i]) / float(len(allDayByTmp[i])))
    print(sum(allDayByTmp1[i]) / float(len(allDayByTmp1[i])))
    print(sum(allDayByTmp2[i]) / float(len(allDayByTmp2[i])))
    print("--------")


#list1=[10,20,30,40,50,60]
#list2=[4,5,6,7,8,9]
#c={"a":list1,
#   "b":list2}
#df2=DataFrame(df1)
#print(df1)
#df2=df1.describe() # 統計結果給 df2
#print(df2)

# #開啟要寫入的檔案以及工作表
# writer = ExcelWriter('Tstock_Analysis.xlsx')
# df1.to_excel(writer,'Sheet2')
# workbook = writer.book
# worksheet = writer.sheets['Sheet2']
# worksheet.conditional_format('A1:E90', {'type': '3_color_scale'})
# #畫折線圖
# chart = workbook.add_chart({'type': 'line'})
#
# chart.add_series({'name': '=Sheet2!$C$1','categories': '=Sheet2!$B$2:$B$87',
# 'values': '=Sheet2!$C$2:$C$87'})
# chart.add_series({'name': '=Sheet2!$D$1','categories': '=Sheet2!$B$2:$B$87',
# 'values': '=Sheet2!$D$2:$D$87'})
# chart.add_series({'name': '=Sheet2!$E$1','categories': '=Sheet2!$B$2:$B$87',
# 'values': '=Sheet2!$E$2:$E$87'})
#
# chart.set_x_axis({'name': 'Date'})
# chart.set_y_axis({'name': 'Stock Value', 'major_gridlines': {'visible': False}})
# chart.set_legend({'position': 'top'})
# worksheet.insert_chart('G2: W20', chart)
# writer.save()
