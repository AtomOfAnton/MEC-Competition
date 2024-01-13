#MEC Competition
#Anthony Golubev, Mihir Patel
#13/01/2024

import math
import pandas as pd
df = pd.read_excel(r"C:\Users\Antho\Downloads\Dataset.xlsx")
x = []
for i in range(len(df.iloc[:,0])):
    x.append(i)
datasheetdict = dict([(z,[a, b, c, d, e, f, g, h, i, j, k, l]) for z, a, b, c, d, e, f, g, h, i, j, k, l in zip(x, df.iloc[:,0], df.iloc[:,1], df.iloc[:,2], df.iloc[:,3], df.iloc[:,4], df.iloc[:,5], df.iloc[:,6], df.iloc[:,7], df.iloc[:,8], df.iloc[:,9], df.iloc[:,10], df.iloc[:,11])])

temp = []
for i in datasheetdict.values():
    if i[5] not in temp and i[5]:
        temp.append(i[5])
temp = [x for x in temp if x == x]
print(temp)