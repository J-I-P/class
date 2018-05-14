import pandas_datareader as pdr
import pandas as pd
import datetime
import matplotlib.pyplot as plt

start=datetime.datetime(2017,7,1)
end=datetime.date.today()
data=pdr.get_data_yahoo('2330.tw',start,end) 
print(data.head())

del data['date']
del data['volume']
del data['adjclose']
#high=data['high']
#high.cumsum()
#high.plot()

# plot open,close,high,low: 4-price curves 
#data.cumsum()
data.plot()
plt.title("2330.tw : TSMC")
plt.xlabel("Days")
plt.ylabel("Price")
plt.gca().invert_xaxis() 
plt.show()

