import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("mergedDF.csv",encoding="latin1")

#print(df['GDP in billion current U.S. dollars'])
plt.figure(figsize = (8, 6))
p1=sns.regplot(df['GDP in billion current U.S. dollars'],df['salesVolume'])
#sns.regplot(data=df, x='GDP in billion current U.S. dollars', y='salesVolume', fit_reg=False, marker="+", color="skyblue")
#p1=sns.regplot(data=df, x='GDP in billion current U.S. dollars', y='salesVolume', fit_reg=False, marker="o", color="skyblue", scatter_kws={'s':400})
#p1.text(3+0.2, 4.5, "An annotation", horizontalalignment='left', size='medium', color='black', weight='semibold')
#sns.plt.show()
df=df[df['GDP in billion current U.S. dollars']>649]
df=df.reset_index(drop=True)
#print(df)
for line in range(0,df.shape[0]):
     p1.text(df['GDP in billion current U.S. dollars'][line]+0.2, df['salesVolume'][line], df['State Abbreviation'][line], horizontalalignment='left', color='black',fontsize=6)
#p1.set(xscale="log")

plt.title("Sales Volume vs GDP")
## Save the image
#plt.savefig("../project_web_1.0/img/GDP_salesVolume.png", dpi = 200)