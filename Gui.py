from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name")


def myLabel():
    hello = "Enter Your Name" + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


myButton = Button(root, text="Click Me!", command=myLabel)
myButton.pack()

root.mainloop()
