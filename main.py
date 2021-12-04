import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandastable import Table


df = pd.read_csv('2021offense.csv', sep=r'\s*,\s*', engine='python')
df = df.drop(columns='"Rk')
df = df.drop(columns='EXP"')
df = df.drop(columns='Rate')

def printDataTerminal():
    print(df)


def scatterGraphData():
    print('Enter X-axis Column: ')
    print('Choices:', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD')
    userInputX = input()
    if userInputX not in {'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD'}:
        print('Incorrect axis value. ')
    graphX = df[userInputX]
    print('Enter Y-axis Column: ')
    userInputY = input()
    if userInputY not in {'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD'}:
        print('Incorrect axis value. ')
    graphY = df[userInputY]
    plt.figure(str(userInputX) + ' per ' + str(userInputY))
    plt.xlabel(userInputX)
    plt.ylabel(userInputY)
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.1 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.1 #last df value + 10% of itself
    ax = plt.gca()  # get current axes
    ax.set_xlim([0, lastEntryX])  # set x-axis limits to 150, 400
    ax.set_ylim([0, lastEntryY])  # set y-axis limits to 0, 14
    plt.scatter(graphX, graphY, cmap= 'viridis')
    plt.colorbar()
    plt.show()


def barGraphData():
    print('Enter X-axis Column: ')
    print('Choices:', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD')
    userInputX = input()
    if userInputX not in {'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD'}:
        print('Incorrect axis value. ')
    graphX = df[userInputX]
    print('Enter Y-axis Column: ')
    userInputY = input()
    if userInputY not in {'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD'}:
        print('Incorrect axis value. ')
    graphY = df[userInputY]
    plt.xlabel(userInputX)
    plt.ylabel(userInputY)
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.1 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.1 #last df value + 10% of itself
    ax = plt.gca()  # get current axes
    ax.set_xlim([0, lastEntryX])  # set x-axis limits to 150, 400
    ax.set_ylim([0, lastEntryY])  # set y-axis limits to 0, 14
    plt.bar(graphX, graphY)
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
