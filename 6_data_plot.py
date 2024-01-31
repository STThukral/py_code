import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("data_corr_5.csv")
print(df.to_string())

# data correlation
print(df.corr())

#data plot (used new library matplot lib)
df.plot()
plt.show()
