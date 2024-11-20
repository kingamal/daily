from tkinter import *

window=Tk()
window.title("Pomodoro Timer")

b1=Button(window, text="Start").grid(row=1, column=0)

b2=Button(window, text="Pause").grid(row=1, column=1)

b3=Button(window, text="Reset").grid(row=1, column=2)

window.mainloop()