from tkinter import *
import numpy as np
import time

start = time.time()

Randnumbers = []
root = Tk()
root.geometry("500x500")

def get_random_num(min_num,max_num, num_size):
    random_num = np.random.randint(min_num,max_num, size=num_size)
    return random_num


def get_random_num2(event):
    random_num2 = np.random.randint(1000, size=10)
    array_label.config(text=random_num2)
    globals.Randnumbers = random_num2


def bubbleSort(arr):
    n = len(arr)
    for x in range(n):
        swapped = False
        for y in range(0,n-x-1):
            if arr[y] > arr[y+1]:
                arr[y] ,arr[y+1] = arr[y+1] ,arr[y]
                swapped = True
        if swapped == False :
            break

    array_label.config(text=arr)

def quit_windows():
    root.destroy()



#--------------------button--------------------
button_gen = Button(root, text="Gen random number")
button_gen.bind("<Button-1>", get_random_num2)

button_bubble_sort = Button(root, text="BubbleSort the random number")
button_bubble_sort.bind("<Button-1>", bubbleSort(Randnumbers))

button_quit = Button(root, text="Exit", command=quit_windows)

#--------------------label--------------------
array_label = Label(root, text="")
bubble_sort_label = Label(root, text="")

#--------------------pack--------------------
button_gen.pack()
array_label.pack()
bubble_sort_label.pack()
button_quit.pack(side="bottom")

#--------------------start--------------------
root.mainloop()
