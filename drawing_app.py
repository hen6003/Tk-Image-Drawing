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

def load():
    fileName = user_input_filename.get()
    fileName = fileName.strip()

    ts = t.getscreen()

    img = Image.open(fileName + '.png')
    img.save(fileName + '.gif', 'gif')
    ts.register_shape(fileName + '.gif')
    t.shape(fileName + '.gif')

    down = t.pen()['pendown']

    t.penup()
    cords = t.pos()
    print(cords)
    t.goto(0,0)
    t.showturtle()
    t.stamp()
    t.hideturtle()
    t.goto(cords)

    if down:
        t.pendown()

    os.remove(fileName + '.gif')

def erase_mode():
    erase_button["state"] = 'disabled'
    pen_button["state"] = 'normal'

    t.pencolor('#ffffff')
    t.pensize(10)

def pen_mode():
    pen_button["state"] = 'disabled'
    erase_button["state"] = 'normal'

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

    if (mouseY > 765 or mouseY < 65):
        return

    mouseX -= 450 - 96
    mouseY -= 450 - 66

    t.goto(mouseX, -mouseY)

def click(event):
    mouseY = root.winfo_pointery()

    if (mouseY > 765 or mouseY < 65):
        return

    if (t.pen()['pendown']):
        t.penup()
    else:
        t.pendown()

root = tk.Tk()
root.minsize(700, 770)
root.maxsize(700, 770)
root.title('Tk Image Drawing')
root.option_add('*font', ('comforta', 12, 'bold'))

root.bind('<Button 1>', click)
root.bind('<Motion>', motion)

canvas = tk.Canvas(master = root, width = 700, height = 700)
canvas.grid(row = 1,columnspan=5)

t = turtle.RawTurtle(canvas)
t.speed(0)
t.hideturtle()
t.pensize(3)
t.penup()

user_input_colour = tk.StringVar() 
user_input_filename = tk.StringVar()

tk.Label(master = root, text = '#', width = 1).grid(row = 0, column = 0) # # before colour hex entry
tk.Entry(master = root, text = user_input_colour, width = 6).grid(row = 0, column = 1) # colour hex entry
tk.Button(master = root, text = "Update Colour", command = update_colour).grid(row = 0, column = 2) # updates the colour from colour hex entry
tk.Button(master = root, text = "Clear", command = t.clear).grid(row = 0, column = 3) # clears canvas
erase_button = tk.Button(master = root, text = "Erase", command = erase_mode) # goes into eraser mode
erase_button.grid(row = 0, column = 4)
pen_button = tk.Button(master = root, text = "Pen", state = 'disabled', command = pen_mode) # goes into pen mode
pen_button.grid(row = 0, column = 5)
tk.Entry(master = root, text = user_input_filename, width = 10).grid(row = 2, column = 0) # file name entry
tk.Button(master = root, text = "Save", command = save_as_png).grid(row = 2, column = 1) # saves the file
tk.Button(master = root, text = "Load", command = load).grid(row = 2, column = 2) # loads the file
tk.Button(master = root, text = "Exit", command = root.quit).grid(row = 2, column = 3) # exit app

root.mainloop()