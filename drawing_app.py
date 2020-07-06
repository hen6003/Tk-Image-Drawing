import turtle, os
import tkinter as tk
from PIL import Image

def save_as_png():
    # save postscipt image 
    fileName = user_input_filename.get()
    fileName = fileName.strip()
    if fileName == '':
        print('Failed: Can\'t save file with no characters')
        return
    ts = t.getscreen()
    ts.getcanvas().postscript(file = fileName + ".eps")
    # use PIL to convert to PNG 
    img = Image.open(fileName + '.eps') 
    img.save(fileName + '.png', 'png') 
    os.remove(fileName + '.eps')
    print('Saved ' + fileName + '.png')

def erase_mode():
    t.pencolor('#ffffff')
    t.pensize(10)

def pen_mode():
    if (user_input_colour.get() != ''):
        update_colour()
    else:
        t.pencolor('#000000')
    
    t.pensize(3)

def update_colour():
    t.pencolor('#' + user_input_colour.get())

def motion(event):
    mouseX = root.winfo_pointerx() - root.winfo_rootx()
    mouseY = root.winfo_pointery() - root.winfo_rooty()

    if (mouseY > 750):
        return

    mouseX -= 450 - 96
    mouseY -= 450 - 96

    t.goto(mouseX, -mouseY)

def click(event):
    mouseY = root.winfo_pointery()
    if (mouseY > 700):
        return

    if (t.pen()['pendown']):
        t.penup()
    else:
        t.pendown()

root = tk.Tk()
root.minsize(700, 735)
root.maxsize(700, 735)
root.title('Tk Image Drawing')
root.option_add('*font', ('comforta', 12, 'bold'))

root.bind('<Button 1>', click)
root.bind('<Motion>', motion)

canvas = tk.Canvas(master = root, width = 700, height = 700)
canvas.grid(row = 0,columnspan=9)

t = turtle.RawTurtle(canvas)
t.speed(0)
t.hideturtle()
t.pensize(3)
t.penup()

user_input_colour = tk.StringVar() 
user_input_filename = tk.StringVar()

tk.Label(master = root, text = '#', width = 1).grid(row = 1, column = 0) # # before colour hex entry
tk.Entry(master = root, text = user_input_colour, width = 6).grid(row = 1, column = 1) # colour hex entry
tk.Button(master = root, text = "Update Colour", command = update_colour).grid(row = 1, column = 2) # updates the colour from colour hex entry
tk.Button(master = root, text = "Clear", command = t.clear).grid(row = 1, column = 3) # clears canvas
tk.Button(master = root, text = "Erase", command = erase_mode).grid(row = 1, column = 4) # goes into eraser mode
tk.Button(master = root, text = "Draw", command = pen_mode).grid(row = 1, column = 5) # goes into pen mode
tk.Entry(master = root, text = user_input_filename, width = 10).grid(row = 1, column = 6) # file name entry
tk.Button(master = root, text = "Save", command = save_as_png).grid(row = 1, column = 7) # saves the file
tk.Button(master = root, text = "Exit", command = root.quit).grid(row = 1, column = 8) # exit app

root.mainloop()