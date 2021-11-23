import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandastable import Table


df = pd.read_csv('2021offense.csv', sep=r'\s*,\s*', engine='python')
df = df.drop(columns='"Rk')
df = df.drop(columns='EXP"')


ax = plt.gca()  # get current axes

ax.set_xlim([0, 500])  # set x-axis limits to 150, 400
ax.set_ylim([0, 50])  # set y-axis limits to 0, 14

plt.xlabel('Cmp')
plt.ylabel('TD')


# ----------------------------------------------------------------
# Misc Code:
#import sqlite3
#headers = ['Rk','Tm','G','Cmp','Att','Cmp%','Yds',"TD","TD%","Int","Int%","Lng","Y/A","AY/A",'Y/C','Y/G','Rate','Sk','Yds','NY/A','ANY/A','Sk%','4QC','GWD','EXP']
#df = df.sort_values(ascending=False)
#plt.plot(x, y, color='red')
#df = df.query('Sk%'> 5.0, inplace = False)

#df.assign(AttPerSack=lambda x: df['Att'] / df['Sk%'])


# ----------------------------------------------------------------
