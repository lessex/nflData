#import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import tkinter as tk


#headers = ['Rk','Tm','G','Cmp','Att','Cmp%','Yds',"TD","TD%","Int","Int%","Lng","Y/A","AY/A",'Y/C','Y/G','Rate','Sk','Yds','NY/A','ANY/A','Sk%','4QC','GWD','EXP']
df = pd.read_csv('2021offense.csv', sep=r'\s*,\s*', engine = 'python')
df = df.drop(columns='"Rk')
df = df.drop(columns='EXP"')

attDF = df['Att']
sacksDF = df['Sk%']
#z = df[''] do att/cmp
df = sacksDF.sort_values(ascending=False)
#plt.plot(x, y, color='red')
#df = df.query('Sk%'> 5.0, inplace = False)
ax = plt.plot(attDF, sacksDF)
ax = plt.gca() #get current axes
ax.set_xlim([150, 400]) #set x-axis limits to 150, 400
ax.set_ylim([0, 14]) #set y-axis limits to 0, 14
plt.xlabel('Att')
plt.ylabel('Sk%') #might have to compute sk/att stat separately
plt.show()
print(df)


#df.sort_index(axis = 1, ascending=True)