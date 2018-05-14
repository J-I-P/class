import pandas as pd
import numpy as np
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

df['ma30'] = np.NaN
df['ma60'] = np.NaN
df['ma90'] = np.NaN

sum = sum30 = sum60 = sum90 = 0.0
avg = avg30 = avg60 = avg90 = 0.0
cnt30 = cnt60 = cnt90 = 1
miss_cnt30 = miss_cnt60 = miss_cnt90 = 0

def rangeSum(s, d1, d2, count):
    if d2 in df.index.values:
        return s+df['close'][d1]-df['close'][d2]
    else:
        if d2+1 in df.index.values:
            return s+df['close'][d1]-df['close'][d2+count]
        else:
            rangeSum(s, d1, d2+1)


for data in range(datas):
    if data in df.index.values:
        sum += df['close'][data]
        if data<30:
            df['ma30'][data] = round(sum / cnt30, 2)
            df['ma60'][data] = round(sum / cnt60, 2)
            df['ma90'][data] = round(sum / cnt90, 2)
            cnt30 += 1
            cnt60 += 1
            cnt90 += 1
        elif data<60:
            if data==30:
                if data-30 in df.index.values:
                    sum30 = sum - df['close'][data-30]
                else:
                    continue
            else:
                sum30 = rangeSum(sum30, data, data-30-miss_cnt30, miss_cnt30)
            df['ma30'][data] = round(sum30 / 30, 2)
            df['ma60'][data] = round(sum / cnt60, 2)
            df['ma90'][data] = round(sum / cnt90, 2)
            cnt60 += 1
            cnt90 += 1
        elif data<90:
            if data==60:
                if data - 60 in df.index.values:
                    sum60 = sum - df['close'][data-60]
                else:
                    continue
            else:
                sum60 = rangeSum(sum60, data, data-60-miss_cnt60, miss_cnt60)
            sum30 = rangeSum(sum30, data, data-30-miss_cnt30, miss_cnt30)
            df['ma30'][data] = round(sum30 / 30, 2)
            df['ma60'][data] = round(sum60 / 60, 2)
            df['ma90'][data] = round(sum / cnt90, 2)
            cnt90 += 1
        else:
            if data==90:
                if data - 90 in df.index.values:
                    sum90 = sum - df['close'][data-90]
                else:
                    continue
            else:
                sum90 = rangeSum(sum90, data, data-90-miss_cnt90, miss_cnt90)
            sum30 = rangeSum(sum30, data, data-30-miss_cnt30, miss_cnt30)
            sum60 = rangeSum(sum60, data, data-60-miss_cnt60, miss_cnt60)
            df['ma30'][data] = round(sum30 / 30, 2)
            df['ma60'][data] = round(sum60 / 60, 2)
            df['ma90'][data] = round(sum90 / 90, 2)
    else:
        miss_cnt30 += 1
        miss_cnt60 += 1
        miss_cnt90 += 1


#df["ma30"] = np.round(df["close"].rolling(window = 30, center = False).mean(), 2)
#df["ma60"] = np.round(df["close"].rolling(window = 60, center = False).mean(), 2)
#df["ma90"] = np.round(df["close"].rolling(window = 90, center = False).mean(), 2)


#sum = 0
#for i in range(90):
#    sum += df['close'][i]
#    tmp = np.round(sum/(i+1), 2)
#    if i < 30:
#        df['ma30'][i] = tmp
#        df['ma60'][i] = tmp
#        df['ma90'][i] = tmp
#    elif i < 60:
#        df['ma60'][i] = tmp
#        df['ma90'][i] = tmp
#    else:
#        df['ma90'][i] = tmp

df.plot()
plt.title("2454.tw")
plt.xlabel("Days")
plt.ylabel("Price")
plt.gca().invert_xaxis()
plt.show()
writer = pd.ExcelWriter('stock2454.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()