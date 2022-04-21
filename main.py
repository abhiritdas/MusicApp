import tkinter as tk
import os
import random
from pygame import mixer

canvas = tk.Tk()
canvas.title("Staff Notes")
canvas.geometry("400x600")
canvas.config(bg = "black")
rootpath = "C:\\Users\\abhir\\Documents_Local\\MusicApp\\Audio"

mixer.init()

class Audio:
    def __init__(self):
        self.random_folder = random.choice(os.listdir(rootpath+"\\"))
        self.random_file = random.choice(os.listdir(rootpath+"\\"+self.random_folder+"\\"))
        self.audio_directory = rootpath+"\\"+self.random_folder+"\\"+self.random_file


def which_button(button_press):
    print(button_press)

def play_audio():
    a = Audio()
    print(a.random_file)
    mixer.music.load(a.audio_directory)
    mixer.music.play()
    
Play = tk.Button(canvas, text="PLAY", command=play_audio)
A = tk.Button(canvas, text ="A", command=lambda m="A": which_button(m))
B = tk.Button(canvas, text ="B", command=lambda m="B": which_button(m))
C = tk.Button(canvas, text ="C", command=lambda m="C": which_button(m))
D = tk.Button(canvas, text ="D", command=lambda m="D": which_button(m))
E = tk.Button(canvas, text ="E", command=lambda m="E": which_button(m))
F = tk.Button(canvas, text ="F", command=lambda m="F": which_button(m))
G = tk.Button(canvas, text ="G", command=lambda m="G": which_button(m))
Play.pack()
A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
F.pack()
G.pack()
canvas.mainloop()