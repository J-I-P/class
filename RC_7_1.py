#RC_7_1: 上網路抓取股價資料畫高低圖
import pandas as pd
#import pandas.io.data as web
import pandas_datareader as web
import datetime
#下載資料起始日與股票代號
start = datetime.datetime(2016,4,1)
end = datetime.datetime(2016,4,19)
#df = web.DataReader('2330.tw','yahoo',start,end)
df = web.get_data_yahoo('2330.tw',start,end)

#日股價資料寫入excel檔
writer=pd.ExcelWriter('2330.xlsx')
df.to_excel(writer,'2330')
workbook = writer.book
worksheet = writer.sheets['2330']
#畫高低圖
chart = workbook.add_chart({'type': 'stock'})
chart.add_series({'name': '=2330!$C$1','categories': '=2330!$A$2:$A$14','values': '=2330!$C$2:$C$14'})
chart.add_series({'name': '=2330!$D$1','categories': '=2330!$A$2:$A$14','values': '=2330!$D$2:$D$14'})
chart.add_series({'name': '=2330!$F$1','categories': '=2330!$A$2:$A$14','values': '=2330!$F$2:$F$14'})
chart.set_title ({'name': 'High-Low-Close'})
chart.set_x_axis({'name': 'Date'})
chart.set_y_axis({'name': 'Share price'})
worksheet.insert_chart('I2', chart)
writer.save()