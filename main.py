import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandastable import Table


df = pd.read_csv('2021offense.csv', sep=r'\s*,\s*', engine='python')
df = df.drop(columns='"Rk')
df = df.drop(columns='EXP"')


attDF = df['Att']
sacksDF = df['Sk%']

# ax = plt.plot(attDF)
ax = plt.gca()  # get current axes
ax.set_xlim([150, 400])  # set x-axis limits to 150, 400
# ax.set_ylim([0, 14])  # set y-axis limits to 0, 14
plt.xlabel('Att')
plt.ylabel('Sk%')
plt.show()
# print(df)

# fn that takes current df & outputs graph, called with button


def printData():
    #df = plt.plot(attDF)
    print(df)  # working, outputs filtered pandastable data to terminal


def graphData():
    ax = plt.plot(attDF)
    plt.show()

# ----------------------------------------------------------------
# Misc Code:
#import sqlite3
#headers = ['Rk','Tm','G','Cmp','Att','Cmp%','Yds',"TD","TD%","Int","Int%","Lng","Y/A","AY/A",'Y/C','Y/G','Rate','Sk','Yds','NY/A','ANY/A','Sk%','4QC','GWD','EXP']
#df = df.sort_values(ascending=False)
#plt.plot(x, y, color='red')
#df = df.query('Sk%'> 5.0, inplace = False)

#df.assign(AttPerSack=lambda x: df['Att'] / df['Sk%'])


# ----------------------------------------------------------------
