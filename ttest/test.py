import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.Series(np.random.randn(100).cumsum())
data.plot()
plt.title("随机累计和折线图")
plt.xlabel("索引")
plt.ylabel("值")
plt.grid(True)
plt.show()
