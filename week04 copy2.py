import pandas as pd
#import numpy as np
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt
start = datetime.datetime(2017,1,1)
end = datetime.datetime.today()
df = web.get_data_yahoo('2454.tw', start, end)

datas = len(df)+3
del df['date']
del df['volume']
del df['high']
del df['low']
del df['open']
#del df['close']
del df['adjclose']

df["ma30"] = round(df["close"].rolling(window = 30, center = False, min_periods=1).mean(), 2)
df["ma60"] = round(df["close"].rolling(window = 60, center = False, min_periods=1).mean(), 2)
df["ma90"] = round(df["close"].rolling(window = 90, center = False, min_periods=1).mean(), 2)


df.plot()
plt.title("2454.tw")
plt.xlabel("Days")
plt.ylabel("Price")
plt.gca().invert_xaxis()
plt.show()
writer = pd.ExcelWriter('stock2454 copy.xlsx')
df.to_excel(writer,'Sheet2')
writer.save()