import pandas as pd
import matplotlib.pyplot as plt
import numpy as  np

data=pd.Series(np.random.randn(100),index=np.arange(100))

print(data)
data.cumsum()
data.plot()
plt.show()

