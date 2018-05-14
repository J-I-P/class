import pandas as pd
import matplotlib.pyplot as plt

datas = [[65, 92, 78, 83, 70], [90, 72, 76, 93, 56], [81, 85, 91, 89, 77], [79, 53, 47, 94, 80]]
indexs = ["Tom", "Charly", "Linda", "Anna"]
columns = ["Chinese","Math","English","Science","PE"]

df = pd.DataFrame(datas, index=indexs, columns=columns)

#df.cumsum()
df.plot()
plt.show()
