import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table

df = pd.read_csv('2021offense.csv', sep=r'\s*,\s*', engine='python') #read in database (any .csv file)
df = df.drop(columns='"Rk') #remove non-useful columns from database
df = df.drop(columns='EXP"')
df = df.drop(columns='Rate')

def printDataTerminal(): #output current database directly to terminal
    print(df)


def queryDB():
    from gui import queryEntry
    userInputQuery = queryEntry.get() #gathers user's string input to queryEntry box
    queryDf = df.query(userInputQuery) #create a new df based on query
    print(queryDf) #output query to terminal


def scatterGraphData(): #outputs scatterplot based on user's input for x & y axes
    from gui import xAxisEntry
    userInputX = xAxisEntry.get() #gather user's input for x-axis
    graphX = df[userInputX] #create a new dataframe based on user's entered x-axis
    from gui import yAxisEntry
    userInputY = yAxisEntry.get() #gather user's input for y-axis
    graphY = df[userInputY] #create a new dataframe based on user's entered y-axis
    plt.figure(str(userInputX) + ' per ' + str(userInputY)) #sets the window title to entered axes
    plt.xlabel(userInputX) #labels x-axis based on user input
    plt.ylabel(userInputY) #labels y-axis based on user input
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.3 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.3 #last df value + 10% of itself
    firstEntryX = graphX.min()  #gathers lowest x-axis entry as first point
    firstEntryY = graphY.min()  #gathers lowest y-axis entry as first point
    ax = plt.gca()  # get current axes
    ax.set_xlim([firstEntryX, lastEntryX])  # set x-axis limits to first & last entries
    ax.set_ylim([firstEntryY, lastEntryY])  # set x-axis limits to first & last entries
    for i in range (len(graphX)):   #labels scatterplot points with each team name
        plt.text(x = graphX[i], y = graphY[i] + 0.1, s = df.Tm[i], fontdict=dict(color = 'black', size = 10), bbox = dict(facecolor='cyan', edgecolor='black', boxstyle='round,pad=0.5', alpha = 0.5))
    plt.scatter(graphX, graphY, cmap= 'viridis')
    plt.show() #show the graph


def barGraphData(): #outputs scatterplot based on user's input for x & y axes
    from gui import xAxisEntry, yAxisEntry
    userInputX = xAxisEntry.get() #gather user's input for x-axis
    graphX = df[userInputX] #create a new dataframe based on user's entered x-axis
    userInputY = yAxisEntry.get() #gather user's input for y-axis
    graphY = df[userInputY] #create a new dataframe based on user's entered y-axis
    plt.figure(str(userInputX) + ' per ' + str(userInputY)) #sets the window title to entered axes
    plt.xlabel(userInputX) #labels x-axis based on user input
    plt.ylabel(userInputY) #labels y-axis based on user input
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.3 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.3 #last df value + 10% of itself
    firstEntryX = graphX.min()  #gathers lowest x-axis entry as first point
    firstEntryY = graphY.min()  #gathers lowest y-axis entry as first point
    ax = plt.gca()  # get current axes
    ax.set_xlim([firstEntryX, lastEntryX])  # set x-axis limits lowest x-axis entry
    ax.set_ylim([firstEntryY, lastEntryY])  # set y-axis limits to lowest y-axis entry
    for i in range (len(graphX)):   #labels scatterplot points with each team name
        plt.text(x = graphX[i], y = graphY[i], s = df.Tm[i], fontdict=dict(color = 'black', size = 10), bbox = dict(facecolor='cyan', edgecolor='black', boxstyle='round,pad=0.5', alpha = 0.5), rotation = 90)
    bars = plt.bar(graphX, graphY) #create bar graph from user input
    for i in range(len(bars)): #loops through bars on bar graph & assigns a color
        bars[i].set_color('xkcd:baby blue')
    plt.show() #show the graph
