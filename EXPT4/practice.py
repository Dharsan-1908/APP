from tkinter import *

from mysqlx import Column
app = Tk()

app.title("You nab")

Label(app, text="Regno").grid(row=0, column=0)
Entry(app).grid(row=0, column=1)

Label(app, text="Gender").grid(row=1, column=0)
var = IntVar()

Radiobutton(app, text="Male", variable=var, value=1).grid(row=2, column=0)
Spinbox(app, from_=19, to=100).grid(row=3, column=0)
app.geometry("400x500")
app.mainloop()
