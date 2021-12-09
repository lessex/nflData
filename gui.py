import tkinter as tk
import main as main
from pandastable import Table
from main import df


root = tk.Tk() #create root window for gui

frame = tk.Frame(root) #create frame for main gui window
frame.pack() #place the frame within gui
root.title('NFL Data') #set title of root window
bottomFrame = tk.Frame(root) #create bottomFrame
bottomFrame.pack(side="bottom") #place bottomFrame at bottom of gui

xAxis = "Default0" #initializing string, will be overwritten with user's input
yAxis = "Default1" #initializing string, will be overwritten with user's input
userQuery = "Att > 300" #initializing string, will be overwritten with user's input


xAxisLabel = tk.Label(root, text = 'X-Axis: ',font=('calibre',10, 'bold'), fg= "black") #display "X-Axis: " text within gui window
yAxisLabel = tk.Label(root, text = 'Y-Axis: ',font=('calibre',10, 'bold'), fg= "black") #display "Y-Axis: " text within gui window
xAxisEntry = tk.Entry(root, textvariable = xAxis, font=('calibre',10,'normal'), bg= "white", fg= "black", width=10) #gather input from user for x-axis
yAxisEntry = tk.Entry(root, textvariable = yAxis, font=('calibre',10,'normal'), bg= "white", fg = "black", width=10) #gather input from user for y-axis
queryLabel = tk.Label(root, text = 'Enter Query: ',font=('calibre',10, 'bold'), fg= "black", width = 10) #display "Enter Query: " text within gui window
queryEntry = tk.Entry(root, textvariable = userQuery, font=('calibre',10,'normal'), bg= "white", fg = "black") #gather input from user for query

#'Query the DB' button on gui, when pressed queryDB() is executed
queryButton = tk.Button(
    root, 
    text = 'Query the DB', 
    fg= "black", 
    command=main.queryDB
)
#'Output to terminal' button on gui, when pressed printDataTerminal() is executed
terminalButton = tk.Button(
    frame,
    text="Output to terminal",
    width=20,
    height=5,
    bg="black",
    fg="black",
    command=main.printDataTerminal
)
#'Scatter Plot' button on gui, when pressed scatterGraphData() is executed
scatterButton = tk.Button(
    frame,
    text="Scatter plot",
    width=12,
    height=5,
    bg="black",
    fg="black",
    command=main.scatterGraphData
)
#'Bar Graph' button on gui, when pressed queryDB() is executed
barButton = tk.Button(
    frame,
    text="Bar plot",
    width=12,
    height=5,
    bg="black",
    fg="black",
    command=main.barGraphData
)
#pack buttons into gui
terminalButton.pack(side='right')
scatterButton.pack(side='left')
barButton.pack(side='left')
queryButton.pack(side='right')
xAxisLabel.pack(side = 'left')
xAxisEntry.pack(side = 'left')
yAxisLabel.pack(side = 'left')
yAxisEntry.pack(side = 'left')
queryLabel.pack(side = 'left')
queryEntry.pack(side = 'left')


pt = Table(bottomFrame, dataframe=df) #create our table from dataframe
pt.show() #display table
df.update(df) #update current database

root.mainloop() #execute entire gui.py file