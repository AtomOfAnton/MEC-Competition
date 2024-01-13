#MEC Competition
#Anthony Golubev, Mihir Patel
#13/01/2024

import math
import pandas as pd
from difflib import SequenceMatcher



df = pd.read_excel(r"C:\Users\Antho\Downloads\Dataset.xlsx")
x = []
for i in range(len(df.iloc[:,0])):
    x.append(i)
datasheetdict = dict([(z,[a, b, c, d, e, f, g, h, i, j, k, l, 0]) for z, a, b, c, d, e, f, g, h, i, j, k, l in zip(x, df.iloc[:,0], df.iloc[:,1], df.iloc[:,2], df.iloc[:,3], df.iloc[:,4], df.iloc[:,5], df.iloc[:,6], df.iloc[:,7], df.iloc[:,8], df.iloc[:,9], df.iloc[:,10], df.iloc[:,11])])

def similarity(x, y):
    return SequenceMatcher(x, y).ratio()

def levenshtein_similarity(x, y):
    a, b = len(x), len(y)
    #makes empty array 
    arr = [[0 for i in range(b+1)] for i in range(a+1)]
    #sets base cases (distance between empty set and string)
    for i in range(a+1):
        arr[i][0] = i
    for j in range(b+1):
        arr[0][j] = j

    for i in range(1, a+1):
        for j in range(1, b+1):
            #checks equality, else adds an operation
            if x[i-1]==y[j-1]:
                arr[i][j] = arr[i-1][j-1]

            else:
                arr[i][j] = 1 + min(arr[i][j-1], arr[i-1][j-1], arr[i-1][j])
    #returns similarity as percentage
    return max((b-arr[a][b])/a, (a-arr[a][b])/b)
    

#convert all salaries to yearly
temp = []
for i in datasheetdict.values():
    if str(i[6]).lower() == "hourly":
        i[5] = i[5]*2087 #average work hours in a year
    elif str(i[6]).lower() == "monthly":
        i[5] = i[5]*12 #average number of months in a year (no discrepancies so far :)
    if i[10] not in temp:
        temp.append(i[11])
temp = [x for x in temp if x == x]


#attributes in order of priority: skills, accessibility features, experience required, job type (full/part-time), min yearly salary