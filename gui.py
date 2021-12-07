import tkinter as tk
import main as main
from pandastable import Table
from main import df


root = tk.Tk()


frame = tk.Frame(root)
frame.pack()
root.title('NFL Data')
bottomFrame = tk.Frame(root)
bottomFrame.pack(side="bottom")

xAxis = "Default0"
yAxis = "Default1"
userQuery = "Att > 300"


xAxisLabel = tk.Label(root, text = 'X-Axis: ',font=('calibre',10, 'bold'), fg= "black")
yAxisLabel = tk.Label(root, text = 'Y-Axis: ',font=('calibre',10, 'bold'), fg= "black")
xAxisEntry = tk.Entry(root, textvariable = xAxis, font=('calibre',10,'normal'), bg= "white", fg= "black", width=10)
yAxisEntry = tk.Entry(root, textvariable = yAxis, font=('calibre',10,'normal'), bg= "white", fg = "black", width=10)
queryLabel = tk.Label(root, text = 'Enter Query: ',font=('calibre',10, 'bold'), fg= "black", width = 10)
queryEntry = tk.Entry(root, textvariable = userQuery, font=('calibre',10,'normal'), bg= "white", fg = "black")


cols = ['Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A',
        'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']

queryButton = tk.Button(root, text = 'Query the DB', fg= "black", command=main.queryDB)


terminalButton = tk.Button(
    frame,
    text="Output to terminal",
    width=20,
    height=5,
    bg="black",
    fg="black",
    command=main.printDataTerminal
)
scatterButton = tk.Button(
    frame,
    text="Scatter plot",
    width=12,
    height=5,
    bg="black",
    fg="black",
    command=main.scatterGraphData
)
barButton = tk.Button(
    frame,
    text="Bar plot",
    width=12,
    height=5,
    bg="black",
    fg="black",
    command=main.barGraphData
)

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


pt = Table(bottomFrame, dataframe=df)
pt.show()
df.update(df)

# plt.show()
root.mainloop()

# ---------------------------------------------------

# root = tk.Tk()
# label = tk.Label(text="Name")
# entry = tk.Entry()
# label.pack()
# entry.pack()
# root.mainloop()
# ---------------------------------------------------

# root = tk.Tk()
# text_box = tk.Text()
# text_box.pack()
# root.mainloop()
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
