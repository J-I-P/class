#E_7_15: 上網路抓取股價資料
import pandas as pd
#import pandas.io.data as web
import pandas_datareader as web
import datetime
#下載資料起始日與股票代號
start = datetime.datetime(2000,1,1)
end = datetime.datetime(2016,4,19)
#df = web.DataReader('2330.tw','yahoo',start,end)
df=web.get_data_yahoo('2330.tw',start,end)

#日股價資料寫入excel檔
writer=pd.ExcelWriter('stock2330.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()