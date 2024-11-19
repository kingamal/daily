from tkinter import *

window=Tk()

def pick_color():
    print('color')

b1=Button(window, text="Pick Color", command=pick_color).grid(row=1, column=0)

l1=Label(window, text="Brush Size: ").grid(row=1, column=1)

b2=Button(window, text="Clear", command=pick_color).grid(row=1, column=2)

b3=Button(window, text="Save Drawing", command=pick_color).grid(row=1, column=3)

b4=Button(window, text="Exit", command=window.destroy).grid(row=1, column=4)

window.mainloop()