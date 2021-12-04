import tkinter as tk
from matplotlib import container
import pandas as pd
from pandastable import Table
from main import df
import matplotlib.pyplot as plt
from main import barGraphData
from main import scatterGraphData
from main import printDataTerminal


root = tk.Tk()


frame = tk.Frame(root)
frame.pack()
root.title('NFL Data')
bottomFrame = tk.Frame(root)
bottomFrame.pack(side="bottom")

cols = ['Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng', 'Y/A',
        'AY/A', 'Y/C', 'Y/G', 'Sk', 'Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']
insideVal = tk.StringVar(root)
insideVal.set("Select an option: ")
dropDown = tk.OptionMenu(root, insideVal, *cols)

def setX():
    graphX = df[insideVal.get()]


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
dropDown.pack(side='top')


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
