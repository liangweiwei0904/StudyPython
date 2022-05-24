import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("score.xlsx")
print(df)
df.dropna()
df1 = df.iloc[0:,1:]
print(df1)
df1.boxplot()
plt.show()
