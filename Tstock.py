#使用pandas套件讀寫excel檔案, ref:E_7_12.py
import pandas as pd
from pandas import ExcelWriter

#from pandas import DataFrame
#運算敘述統計
df1=pd.read_excel('Tstock_Data.xlsx', sheetname='report1', skiprows=0)
#list1=[10,20,30,40,50,60]
#list2=[4,5,6,7,8,9]
#c={"a":list1,
#   "b":list2}
#df2=DataFrame(df1)

df2=df1.describe() # 統計結果給 df2
print(df2)

#開啟要寫入的檔案以及工作表
writer = ExcelWriter('Tstock_Analysis.xlsx')
df1.to_excel(writer,'Sheet2')
workbook = writer.book
worksheet = writer.sheets['Sheet2']
worksheet.conditional_format('A1:E90', {'type': '3_color_scale'})
#畫折線圖
chart = workbook.add_chart({'type': 'line'})

chart.add_series({'name': '=Sheet2!$C$1','categories': '=Sheet2!$B$2:$B$87',
'values': '=Sheet2!$C$2:$C$87'})
chart.add_series({'name': '=Sheet2!$D$1','categories': '=Sheet2!$B$2:$B$87',
'values': '=Sheet2!$D$2:$D$87'})
chart.add_series({'name': '=Sheet2!$E$1','categories': '=Sheet2!$B$2:$B$87',
'values': '=Sheet2!$E$2:$E$87'})

chart.set_x_axis({'name': 'Date'})
chart.set_y_axis({'name': 'Stock Value', 'major_gridlines': {'visible': False}})
chart.set_legend({'position': 'top'})
worksheet.insert_chart('G2: W20', chart)
writer.save()
