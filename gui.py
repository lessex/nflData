import tkinter as tk
from pandastable import Table
from main import graphData, printData
from main import df
import matplotlib.pyplot as plt


window = tk.Tk()


frame = tk.Frame(window)
frame.pack()

bottomFrame = tk.Frame(window)
bottomFrame.pack(side = "bottom")


button1 = tk.Button(
    frame,
    text="Output to terminal",
    width=20,
    height=5,
    bg="black",
    fg="black",
    command=printData
)
button2 = tk.Button(
    frame,
    text="Output to graph",
    width=20,
    height=5,
    bg="black",
    fg="black",
    command=graphData
)

# label.pack()
button1.pack(side='right')
button2.pack(side='left')

pt = Table(bottomFrame, dataframe=df)
pt.show()
#plt.show()
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
