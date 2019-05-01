# import tkinter as tk
#
# class Draw:
#
#     def __init__(self):
#
#         self.root = tk.Tk()
#         self.root.maxsize(800, 800)
#         self.root.minsize(800, 800)
#
#         self.c = tk.Canvas(self.root, height=600, width=600, bg="#fdffb7")
#         self.c.pack()
#         self.root.mainloop()
#
#
# draw = Draw()

from tkinter import *

def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#ff0000")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#ff0000")

def draw_rectangles(canvas, line_distance):
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_rectangle(x, 0, 49, 49, fill="black")
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_rectangle(0, y, 49, 49, fill="black")

master = Tk()
canvas_width = 600
canvas_height = 600
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

checkered(w,50)
w.create_rectangle(49, 49, 99, 99, fill="black")


mainloop()