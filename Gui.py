from tkinter import *

root = Tk()


def myLabel():
    my_label = Label(root, text="আমার নাম সুশেন বিশ্বাস")
    my_label.pack()


myButton = Button(root, text="Click Me!", command=myLabel)
myButton.pack()

root.mainloop()
