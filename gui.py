import tkinter as tk
import pandas as pd
from pandastable import Table
from main import df
import matplotlib.pyplot as plt
from main import barGraphData
from main import scatterGraphData
from main import printDataTerminal


window = tk.Tk()


frame = tk.Frame(window)
frame.pack()
window.title('NFL Data')
bottomFrame = tk.Frame(window)
bottomFrame.pack(side="bottom")


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
