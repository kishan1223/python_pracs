import tkinter
from tkinter import *
 
window = tkinter.Tk()


C = tkinter.Canvas(window, bg="red", height=250, width=300)
C.pack()

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
 
# to rename the title of the window window.title("GUI")
 
# pack is used to show the object in the window

label = tkinter.Label(window, text = "Hello World!", font=("Arial Bold", 50)).pack()
 
window.mainloop()
