from tkinter import *
from functools import partial

window = Tk()
window.title("Convert Miles to Kilometers")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# Miles

def label(text, column, row):
    my_label = Label(text=f"{text}", font=("Arial", 14, "bold"))
    my_label.grid(column=column, row=row)


# Entry
number = StringVar()
input = Label(window, width=20)
input.pack(pady=20)
input.grid(column=2, row=1)
entryNum = Entry(window, textvariable=number, width=10)
entryNum.grid(column=2, row=1)

# Is equal
label("Is equal to", 1, 2)
label("Miles", 3, 1)


# Is equal
def call_result(n1):
    numb = (n1.get())
    result = float(numb) * 1.609
    label(result, 2, 2)
    return


label("Km", 3, 2)

# Button
call_result = partial(call_result, number)
button = Button(text="Calculate", command=call_result)
button.grid(column=2, row=3)

window.mainloop()
