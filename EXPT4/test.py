import tkinter as tk
window = tk.Tk()
word = tk.Label(text="hii,hello.... ")
label = tk.Label(text="click the bleow button", background="#34A2FE")
label1 = tk.Label(text="this is a new one")
button = tk.Button(text="clisk me noob!!", width=25,height=5,bg="black",fg="white")
entry = tk.Entry()
password = tk.StringVar()
password_entry = tk.Entry(
    textvariable=password,
    show='*'
)
password_entry.pack()
word.pack()
label.pack()
button.pack()
entry.pack()
label1.pack()
window.mainloop()