from tkinter import *
import time

work_time = 1 * 60
short_break = 5 * 60
long_break = 15 * 60
current_timer = None
paused = False
pause_time = 0
pomodoro_count = 0

def start_timer():
    global paused, pause_time
    if paused and pause_time > 0:
        paused = False
        countdown(pause_time)
    else:
        countdown(work_time)

def pause_timer():
    global paused, pause_time
    paused = True

def reset_timer():
    global current_timer, paused, pomodoro_count, pause_time
    if current_timer:
        window.after_cancel(current_timer)
    paused = False
    pause_time = 0
    pomodoro_count = 0
    canvas.itemconfig(timer_text, text="00:00")

def countdown(count):
    global current_timer, paused, pause_time, pomodoro_count
    if paused:
        pause_time = count
        return
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        current_timer = window.after(1000, countdown, count - 1)
    else:
        pomodoro_count += 1
        if pomodoro_count % 4 == 0:
            show_break_message(long_break, "Take a long break!")
        else:
            show_break_message(short_break, "Take a short break!")

def show_break_message(break_time, message):
    def on_ok():
        break_window.destroy()
        countdown(break_time)

    break_window = Toplevel(window)
    break_window.title("Break Time!")
    break_window.geometry("300x400")
    break_window.config(padx=20, pady=20, bg="white")
    
    message_label = Label(
        break_window, 
        text=message, 
        font=("Courier", 14, "bold"), 
        bg="white", 
        fg="green"
    )
    message_label.pack(pady=10)

    ok_button = Button(break_window, text="OK", command=on_ok)
    ok_button.pack(pady=20)

window=Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="#f7f5dd")

canvas = Canvas(window, width=200, height=224, bg="#f7f5dd", highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="00:00", fill="black", font=("Courier", 35, "bold"))
canvas.grid(row=0, column=1)

b1=Button(window, text="Start", font=("Courier", 10, "bold"), command=start_timer).grid(row=1, column=0)

b2=Button(window, text="Pause", font=("Courier", 10, "bold"), command=pause_timer).grid(row=1, column=1)

b3=Button(window, text="Reset", font=("Courier", 10, "bold"), command=reset_timer).grid(row=1, column=2)

window.mainloop()