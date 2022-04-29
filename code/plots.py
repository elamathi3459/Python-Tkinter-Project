from tkinter import *
from data import *
from tkinter import messagebox
import matplotlib.pyplot as plt 
import numpy as np

s = df[['primary_type']] #  get a series from data frame
crime_count = pd.DataFrame(s.groupby('primary_type').size().sort_values(ascending=True).rename('counts'))
data=crime_count.iloc[-10:-5] # retrieving select rows by loc method
print(data[::-1]) 
data.plot(kind='barh')
plt.subplots_adjust(left=0.33, right=0.89) 
# Show graphic
plt.show()
 
import time
import datetime
start = datetime.datetime.strptime("2019-1-1","%Y-%m-%d").date()
end = datetime.datetime.strptime("2019-3-31","%Y-%m-%d").date()

df['date'] = pd.to_datetime(df.date)
df['date'] = pd.to_datetime(df['date']).dt.date

s = df[['arrest']] #  get a series from data frame
arrest_count = pd.DataFrame(s.groupby('arrest').size().sort_values(ascending=True).rename('counts'))
print(crime_count)

y = np.array([248, 752])
mylabels = ["Arrested", "Non Arrested"]

plt.pie(y, labels = mylabels,autopct='%1.1f%%')
plt.legend()
plt.show() 

