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


def queryDB():
    from gui import queryEntry
    userInputQuery = queryEntry.get()
    queryDf = df.query(userInputQuery)
    print(queryDf)


def scatterGraphData():
    from gui import xAxisEntry
    userInputX = xAxisEntry.get()
    graphX = df[userInputX]
    from gui import yAxisEntry
    userInputY = yAxisEntry.get()
    graphY = df[userInputY]
    plt.figure(str(userInputX) + ' per ' + str(userInputY))
    plt.xlabel(userInputX)
    plt.ylabel(userInputY)
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.1 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.1 #last df value + 10% of itself
    ax = plt.gca()  # get current axes
    ax.set_xlim([0, lastEntryX])  # set x-axis limits to 150, 400
    ax.set_ylim([0, lastEntryY])  # set y-axis limits to 0, 14
    for i in range (len(graphX)):   #labels scatterplot points with each team name
        plt.text(x = graphX[i] + 0.2, y = graphY[i] + 0.1, s = df.Tm[i])
    plt.scatter(graphX, graphY, cmap= 'viridis')
    plt.colorbar()
    plt.show()


def barGraphData():
    from gui import xAxisEntry, yAxisEntry
    userInputX = xAxisEntry.get()
    if userInputX not in {'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD'}:
        print('Incorrect axis value. ')
    graphX = df[userInputX]
    userInputY = yAxisEntry.get()
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
    plt.bar(graphX, graphY)
    plt.show()
