from tkinter import *
import random
import string

root = Tk()
root.geometry("400x280")
root.title("Password Generator")

# intro
title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("The strength of Password")


def selection():
    selection = choice.get()


choice = IntVar()
R1 = Radiobutton(root, text="Weak", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="Medium", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="Strong", variable=choice, value=3, command=selection).pack(anchor=CENTER)

labelChoice = Label(root)
labelChoice.pack()

lenLabel = StringVar()
lenLabel.set("Length of the Password")
lenTitle = Label(root, textvariable=lenLabel).pack()

val = IntVar()
spinLength = Spinbox(root, from_=6, to_=12, textvariable=val, width=13).pack()


def callback():
    lsum.config(text=passgen())


passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# logic
weak = string.ascii_uppercase + string.ascii_lowercase
medium = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbol = """`~!@#$%^&*()_+={}[]|\:;"'<>,.?/"""
strong = weak + medium + symbol


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(weak, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(medium, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(strong, val.get()))


root.mainloop()
