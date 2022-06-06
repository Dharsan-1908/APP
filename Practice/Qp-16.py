from tkinter import *

from mysqlx import Column, Result, Row
from pkg_resources import resource_exists

app = Tk()

app.title("Calculator")


def addNum():
    result = int(FirstNum.get()) + int(SecondNum.get())
    resString.set(result)


Label(app, text="First Number").grid(row=0, column=0)
FirstNum = Entry(app)
FirstNum.grid(row=0, column=1)

Label(app, text="Second Number").grid(row=1, column=0)
SecondNum = Entry(app)
SecondNum.grid(row=1, column=1)

resString = StringVar()
Label(app, text="").grid(row=2, column=0)
Entry(app, textvariable=resString).grid(row=2, column=1)

Add = Button(app, text="AddNum", command=addNum).grid(row=3, column=0)
app.mainloop()
