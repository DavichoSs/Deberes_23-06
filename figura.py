#@ALEXANDER FIGUEROA
#PROGRAMA QUE PERMITE MOVER OBJETOS EN UNA INTERFAZ
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.create_rectangle(10, 70, 50, 100, width=5, fill= 'green')
canvas.create_rectangle(20, 130, 50, 150, width=5, fill= 'black')

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -2)
        canvas.move(2, 0, -4)
        canvas.move(3, 0, -6)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 2)
        canvas.move(2, 0, 3)
        canvas.move(3, 0, 6)
    elif event.keysym == 'Left':
        canvas.move(1, -2, 0)
        canvas.move(2, -4, 0)
        canvas.move(3, -6, 0)
    else:
        canvas.move(1, 2, 0)
        canvas.move(2, 4, 0)
        canvas.move(3, 5, 0)

canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
tk.mainloop()