from tkinter import *
import numpy as np
import time

start = time.time()

root = Tk()
root.geometry("500x500")
random_num = []
def get_random_num(min_num,max_num, num_size):
    random_num = np.random.randint(min_num,max_num, size=num_size)
    return random_num


def random_num2():
    random_num2 = np.random.randint(0, 1000, size=10)
    array_label.config(text=random_num2)
    global random_num
    random_num = random_num2
    button_bubble_sort.pack()

def get_random_num2():
    return random_num

def bubble_sort():
    arr = get_random_num2()
    n = len(arr)
    for x in range(n):
        swapped = False
        for y in range(0,n-x-1):
            if arr[y] > arr[y+1]:
                arr[y] ,arr[y+1] = arr[y+1] ,arr[y]
                swapped = True
        if swapped == False :
            break
    bubble_sort_label.config(text=arr)
    bubble_sort_label.pack()

def quit_windows():
    root.destroy()



#--------------------button--------------------
button_gen = Button(root, text="Gen random number", command=random_num2)

button_bubble_sort = Button(root, text="BubbleSort", command=bubble_sort)

button_quit = Button(root, text="Exit", command=quit_windows)

#--------------------label--------------------
array_label = Label(root, text="")
bubble_sort_label = Label(root, text="")
#--------------------pack--------------------
button_gen.pack()
array_label.pack()
button_quit.pack(side="bottom")

#--------------------start--------------------
root.mainloop()
