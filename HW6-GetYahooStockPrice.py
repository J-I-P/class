# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 可能你需安裝 git, pip 套件
# sudo apt-get install git
# 或升級 pip :
# python -m pip install --upgrade pip 

# 可能你需下載套件 pandas_datareader, pandas, ....
# sudo pip install pandas_datareader 
# sudo pip install pandas
# sudo apt-get install python-tk  (視窗)
# sudo pip install matplotlib  (繪圖)
#
# 若仍無法執行, 請下載安裝最新 pandas-datareader.git 套件
# 因 Yahoo 更新 API 可能舊版無法執行
# (參考:https://github.com/pydata/pandas-datareader/issues/507)
#
# sudo pip install git+https://github.com/pydata/pandas-datareader.git
#
import pandas as pd
import pandas_datareader as pdr
import datetime
#下載資料起始日與股票代號
start = datetime.datetime(2000,1,1)
end = datetime.date.today()

# 使用 pdr.get_data_yahoo 
# 取代 pdr.DataReader('2330.tw','yahoo',start,end)
df = pdr.get_data_yahoo('2330.tw',start,end)

print(df.head())
print(df)
