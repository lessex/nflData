import tkinter as tk
import pandas as pd
from pandastable import Table
from main import df
import matplotlib.pyplot as plt


window = tk.Tk()


frame = tk.Frame(window)
frame.pack()
window.title('NFL Data')
bottomFrame = tk.Frame(window)
bottomFrame.pack(side="bottom")


def printDataTerminal():
    print(df)


def scatterGraphData():
    print('Enter X-axis Column: ')
    print('Choices:', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD')
    userInputX = input()
    if userInputX not in {'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD'}:
        print('Incorrect axis value. ')
    graphX = df[userInputX]
    print('Enter Y-axis Column: ')
    userInputY = input()
    if userInputY not in {'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD'}:
        print('Incorrect axis value. ')
    graphY = df[userInputY]
    plt.xlabel(userInputX)
    plt.ylabel(userInputY)
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.1 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.1 #last df value + 10% of itself
    ax = plt.gca()  # get current axes
    ax.set_xlim([0, lastEntryX])  # set x-axis limits to 150, 400
    ax.set_ylim([0, lastEntryY])  # set y-axis limits to 0, 14
    plt.scatter(graphX, graphY)
    plt.show()


def barGraphData():
    plt.xlabel('Att')
    plt.ylabel('TD%')
    graphX = df['Att']
    graphY = df['TD%']
    lastEntryX = graphX.iloc[0] + graphX.iloc[0] * 0.1 #last df value + 10% of itself
    lastEntryY = graphY.iloc[0] + graphY.iloc[0] * 0.1 #last df value + 10% of itself
    ax = plt.gca()  # get current axes
    ax.set_xlim([0, lastEntryX])  # set x-axis limits to 150, 400
    ax.set_ylim([0, lastEntryY])  # set y-axis limits to 0, 14
    plt.bar(graphX, graphY)
    plt.show()


button1 = tk.Button(
    frame,
    text="Output to terminal",
    width=20,
    height=5,
    bg="black",
    fg="black",
    command=printDataTerminal
)
button2 = tk.Button(
    frame,
    text="Scatter plot",
    width=12,
    height=5,
    bg="black",
    fg="black",
    command=scatterGraphData
)
button3 = tk.Button(
    frame,
    text="Bar plot",
    width=12,
    height=5,
    bg="black",
    fg="black",
    command=barGraphData
)

# label.pack()
button1.pack(side='right')
button2.pack(side='left')
button3.pack(side='left')


pt = Table(bottomFrame, dataframe=df)
pt.show()
df.update(df)

# plt.show()
window.mainloop()

# ---------------------------------------------------

# window = tk.Tk()
# label = tk.Label(text="Name")
# entry = tk.Entry()
# label.pack()
# entry.pack()
# window.mainloop()
# ---------------------------------------------------

# window = tk.Tk()
# text_box = tk.Text()
# text_box.pack()
# window.mainloop()
# ---------------------------------------------------
# label = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",  # Set the text color to white
#     background="black",  # Set the background color to black
#     width=10,
#     height=10
# )
#entry = tk.Entry(fg="white", bg="black", width=50)
# ---------------------------------------------------
