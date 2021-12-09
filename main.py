import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from pandastable import Table

df = pd.read_csv('2021offense.csv', sep=r'\s*,\s*', engine='python')
df = df.drop(columns='"Rk')
df = df.drop(columns='EXP"')
df = df.drop(columns='Rate')

def printDataTerminal():
    print(df)


def queryDB():
    from gui import queryEntry
    userInputQuery = queryEntry.get() #gathers user's string input to queryEntry box
    queryDf = df.query(userInputQuery) #create a new df based on query
    print(queryDf) #output query to terminal


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
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.3 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.3 #last df value + 10% of itself
    firstEntryX = graphX.min()  #gathers lowest x-axis entry as first point
    firstEntryY = graphY.min()  #gathers lowest y-axis entry as first point
    ax = plt.gca()  # get current axes
    ax.set_xlim([firstEntryX, lastEntryX])  # set x-axis limits to 150, 400
    ax.set_ylim([firstEntryY, lastEntryY])  # set y-axis limits to 0, 14
    for i in range (len(graphX)):   #labels scatterplot points with each team name
        plt.text(x = graphX[i], y = graphY[i] + 0.1, s = df.Tm[i], fontdict=dict(color = 'black', size = 10), bbox = dict(facecolor='cyan', edgecolor='black', boxstyle='round,pad=0.5', alpha = 0.5))
    plt.scatter(graphX, graphY, cmap= 'viridis')
    #plt.colorbar()
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
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.3 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.3 #last df value + 10% of itself
    firstEntryX = graphX.min()  #gathers lowest x-axis entry as first point
    firstEntryY = graphY.min()  #gathers lowest y-axis entry as first point
    ax = plt.gca()  # get current axes
    ax.set_xlim([firstEntryX, lastEntryX])  # set x-axis limits lowest x-axis entry
    ax.set_ylim([firstEntryY, lastEntryY])  # set y-axis limits to lowest y-axis entry
    for i in range (len(graphX)):   #labels scatterplot points with each team name
        plt.text(x = graphX[i], y = graphY[i], s = df.Tm[i], fontdict=dict(color = 'black', size = 10), bbox = dict(facecolor='cyan', edgecolor='black', boxstyle='round,pad=0.5', alpha = 0.5), rotation = 90)
    bars = plt.bar(graphX, graphY)
    for i in range(len(bars)): #loops through bars on bar graph & assigns a color
        bars[i].set_color('xkcd:baby blue')
    plt.show()
