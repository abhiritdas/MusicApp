import tkinter as tk
import os
import random
from pygame import mixer

canvas = tk.Tk()
canvas.title("Staff Notes")
canvas.geometry("400x400")
canvas.config(bg = "black")
rootpath = "C:\\Users\\abhir\\Documents_Local\\MusicApp\\Audio"

mixer.init()

class Audio:
    def __init__(self):
        self.random_folder = random.choice(os.listdir(rootpath+"\\"))
        self.random_file = random.choice(os.listdir(rootpath+"\\"+self.random_folder+"\\"))
        self.audio_directory = rootpath+"\\"+self.random_folder+"\\"+self.random_file

class Main():
    def __init__(self):
        self.audio_ready = True

    def which_button(self, button_press):
        if(button_press==folder):
            correct_label.pack()
            canvas.after(1000, self.hide_label, correct_label)
            self.audio_ready = True
        else:
            incorrect_label.pack()
            canvas.after(1000, self.hide_label, incorrect_label)

    def play_audio(self):
        if(self.audio_ready == True):
            a = Audio()
            global folder
            folder = a.random_folder
            mixer.music.load(a.audio_directory)
            mixer.music.play()
            print(a.random_file)
            self.audio_ready = False
        else:
            mixer.music.play()

    def hide_label(self, label):
        label.forget()
    
main = Main()
Play = tk.Button(canvas, text="PLAY", command=main.play_audio)
A = tk.Button(canvas, text ="A", command=lambda m="A": main.which_button(m))
Bb = tk.Button(canvas, text ="Bb", command=lambda m="Bb": main.which_button(m))
B = tk.Button(canvas, text ="B", command=lambda m="B": main.which_button(m))
C = tk.Button(canvas, text ="C", command=lambda m="C": main.which_button(m))
C_sharp = tk.Button(canvas, text ="C#", command=lambda m="C#": main.which_button(m))
D = tk.Button(canvas, text ="D", command=lambda m="D": main.which_button(m))
Eb = tk.Button(canvas, text ="Eb", command=lambda m="Eb": main.which_button(m))
E = tk.Button(canvas, text ="E", command=lambda m="E": main.which_button(m))
F = tk.Button(canvas, text ="F", command=lambda m="F": main.which_button(m))
F_sharp = tk.Button(canvas, text ="F#", command=lambda m="F#": main.which_button(m))
G = tk.Button(canvas, text ="G", command=lambda m="G": main.which_button(m))
G_sharp = tk.Button(canvas, text ="G#", command=lambda m="G#": main.which_button(m))
correct_label = tk.Label(canvas, text ="CORRECT")
incorrect_label = tk.Label(canvas, text ="INCORRECT, TRY AGAIN")
    
Play.pack()
A.pack()
Bb.pack()
B.pack()
C.pack()
C_sharp.pack()
D.pack()
Eb.pack()
E.pack()
F.pack()
F_sharp.pack()
G.pack()
G_sharp.pack()
canvas.mainloop()