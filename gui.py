import tkinter as tk
#from main import getQuery
window = tk.Tk()
def getQuery():
    print('lets go')
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=10,
    height=10
)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="black",
    fg="black",
    command=getQuery
)
#entry = tk.Entry(fg="white", bg="black", width=50)

# label.pack()
button.pack()
window.mainloop()
#---------------------------------------------------

# window = tk.Tk()
# label = tk.Label(text="Name")
# entry = tk.Entry()
# label.pack()
# entry.pack()
# window.mainloop()
#---------------------------------------------------

# window = tk.Tk()
# text_box = tk.Text()
# text_box.pack()
# window.mainloop()
#---------------------------------------------------