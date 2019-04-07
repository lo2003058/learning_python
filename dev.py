from tkinter import *
import numpy as np
root = Tk()
root.geometry("500x500")

def get_random_num(max_num, num_size):
    random_num = np.random.randint(max_num, size=num_size)
    return random_num


def get_random_num2(event):
    random_num2 = np.random.randint(1000, size=10)
    array_label.config(text=random_num2)


def quit_windows():
    root.destroy()

button_gen = Button(root, text="Gen random number")
button_gen.bind("<Button-1>", get_random_num2)
button_quit = Button(root, text="Exit", command=quit_windows)

array_label = Label(root, text="")
button_gen.pack()
array_label.pack()
button_quit.pack()

root.mainloop()
