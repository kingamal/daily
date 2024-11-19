from tkinter import *

window=Tk()

def pick_color():
    print('color')

b1=Button(window, text="Pick Color", command=pick_color)
b1.grid(row=1, column=0)

l1=Label(window, text="Brush Size: ")
l1.grid(row=1, column=1)

b2=Button(window, text="Clear", command=pick_color)
b2.grid(row=1, column=2)

b3=Button(window, text="Save Drawing", command=pick_color)
b3.grid(row=1, column=3)

b4=Button(window, text="Exit", command=window.destroy)
b4.grid(row=1, column=4)

window.mainloop()