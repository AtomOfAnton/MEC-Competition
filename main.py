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
job_type = df.iloc[:,8]
location = df.iloc[:,9]
experience_level = df.iloc[:,10]
skills = df.iloc[:,11]
accessibility_features = df.iloc[:,12]

importance_order = (skills,accessibility_features,experience_level,job_type, min_salary)
