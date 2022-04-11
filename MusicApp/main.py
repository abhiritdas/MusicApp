import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Staff Notes")
canvas.geometry("400x600")
canvas.config(bg = "white")

listBox = tk.Listbox(canvas, fg= "white" , bg = "black", width = 100, font = ('poppins', 20))
listBox.pack(padx=0, pady=15)

listBox.insert(0, 'C')
listBox.insert(1, 'D')
listBox.insert(2, 'E')
listBox.insert(3, 'F')
listBox.insert(4, 'G')
listBox.insert(5, 'A')
listBox.insert(6, 'B')

canvas.mainloop()