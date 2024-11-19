from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw, ImageTk

window=Tk()
window.title("Basic Drawing App")

brush_color = "black"
brush_size = 1
canvas_width, canvas_height = 800, 500

image = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(image)

def pick_color():
    global brush_color
    color = askcolor(color=brush_color)[1]
    if color:
        brush_color = color

def set_brush_size(value):
    global brush_size
    brush_size = int(value)

def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=brush_color, outline=brush_color)
    draw.ellipse([x1, y1, x2, y2], fill=brush_color, outline=brush_color)

def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, canvas_width, canvas_height], fill="white")

def save_drawing():
    filename = "drawing.png"
    image.save(filename)

canvas = Canvas(window, bg="white", width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=0, columnspan=5)
canvas.bind("<B1-Motion>", paint)

b1=Button(window, text="Pick Color", command=pick_color).grid(row=1, column=0)

l1=Label(window, text="Brush Size: ").grid(row=1, column=1)

brush_size_slider = Scale(window, from_=1, to=5, orient=HORIZONTAL, command=set_brush_size)
brush_size_slider.set(brush_size)
brush_size_slider.grid(row=1, column=2)

b2=Button(window, text="Clear", command=clear_canvas).grid(row=1, column=3)

b3=Button(window, text="Save Drawing", command=save_drawing).grid(row=1, column=4)

b4=Button(window, text="Exit", command=window.destroy).grid(row=1, column=5)

window.mainloop()