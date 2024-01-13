#MEC Competition
#Anthony Golubev, Mihir Patel
#13/01/2024

import math
import pandas as pd
df = pd.read_excel(r"C:\Users\Antho\Downloads\Dataset.xlsx")
datasheetdict = {}
index = df.iloc[:,1]
title = df.iloc[:,2]
description = df.iloc[:,3]
max_salary = df.iloc[:,4]
med_salary = df.iloc[:,5]
min_salary = df.iloc[:,6]
pay_period = df.iloc[:,7]
location = df.iloc[:,8]
experience_level = df.iloc[:,9]
skills = df.iloc[:,10]
accessibiliy_features = df.iloc[:,11]

print(index,title,description,max_salary,med_salary,min_salary,pay_period,location,experience_level,skills,accessibiliy_features)