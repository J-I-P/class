import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.DataFrame(
   np.random.randn(40,4),
   index=np.arange(40),
   columns=list("ABCD")
  )

print(data)
data.cumsum()
data.plot()
plt.show()
