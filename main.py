#MEC Competition
#Anthony Golubev, Mihir Patel
#13/01/2024

import math
import pandas as pd
df = pd.read_excel(r"C:\Users\Antho\Downloads\Dataset.xlsx")
datasheetdict = {}
index = df.iloc[:,0]
title = df.iloc[:,1]
description = df.iloc[:,2]
max_salary = df.iloc[:,3]
med_salary = df.iloc[:,4]
min_salary = df.iloc[:,5]
pay_period = df.iloc[:,6]
job_type = df.iloc[:,7]
location = df.iloc[:,8]
experience_level = df.iloc[:,9]
skills = df.iloc[:,10]
accessibility_features = df.iloc[:,11]

temp = []
print(pay_period.values())
for x in pay_period.values():
    if x not in temp:
        temp.append(x)
print(temp)
importance_order = (skills,accessibility_features,experience_level,job_type, min_salary)
attributes = []
