# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:16:07 2022

@author: aenna
"""

import tkinter as tk
from secrets import choice
from PIL import Image , ImageTk

#Geometric parameters of the game
window = tk.Tk()
window.title("Python Rock Paper Scissor Game")
h= 4
w = 3*h
button_color = "#5d8bf4"
label_color = "#dff6ff"
img = Image.open("taskagitmakas.png").resize((260,148))
im = ImageTk.PhotoImage(img)

# İnitializing game parameters
rock = "ROCK"
paper = "PAPER"
sciss = "SCISSORS"
conditions = [rock,paper,sciss]
winner = ""
comp_choice = ""

# Compare function compares computers choice and yours , then update the labels
def compare(your,comp):
    global comp_choice,conditions
    
    comp_choice = choice(conditions)
    if your == comp_choice :
        you_label.config(text = f"Your : {your}")
        comp_label.config(text = f"Computers : {comp_choice}")
        win_label.config(text = f"DRAW")
        
    elif (your == rock and comp_choice == paper) or (your == paper and comp_choice == rock) :
        winner = paper
        you_label.config(text = f"Your : {your}")
        comp_label.config(text = f"Computers : {comp_choice}")
        if your == winner:
            win_label.config(text = "YOU won")
        else:
            win_label.config(text = "COMPUTER won")
    elif (your == rock and comp_choice == sciss) or (your == sciss and comp_choice == rock) :
        winner = rock
        you_label.config(text = f"Your : {your}")
        comp_label.config(text = f"Computers : {comp_choice}")
        if your == winner:
            win_label.config(text = "YOU won")
        else:
            win_label.config(text = "COMPUTER won")
    elif (your == paper and comp_choice == sciss) or (your == sciss and comp_choice == paper) :
        winner = sciss
        you_label.config(text = f"Your : {your}")
        comp_label.config(text = f"Computers : {comp_choice}")
        if your == winner:
            win_label.config(text = "YOU won")
        else:
            win_label.config(text = "COMPUTER won")
        





# Setting widgets
auto_frame = tk.Frame()
auto_label = tk.Label(master = auto_frame , image = im)
you_label = tk.Label(master = auto_frame , text = "Your :" , width = 3*w , height = h , bg = label_color)
comp_label = tk.Label(master = auto_frame , text = "Computers :" , width = 3*w , height = h , bg = label_color)
win_label = tk.Label(master = auto_frame , text = "Winner is ..." , width = 3*w , height = h , bg = label_color)
buttons_frame = tk.Frame()
rock_b = tk.Button(buttons_frame , text = rock , width = w , height = h , bg = button_color , command = lambda : compare(rock,comp_choice))
paper_b = tk.Button(buttons_frame , text = paper , width = w , height = h , bg = button_color , command = lambda : compare(paper,comp_choice))
sciss_b = tk.Button(buttons_frame , text = sciss , width = w , height = h , bg = button_color , command = lambda : compare(sciss,comp_choice))


# Organizing the geometry          
auto_frame.grid(row = 0 , column = 0)
auto_label.grid(row = 0 , column = 0 )
you_label.grid(row = 1 ,column = 0)
comp_label.grid(row = 2 ,column = 0)
win_label.grid(row = 3 ,column = 0)
buttons_frame.grid( row = 1 , column = 0)
rock_b.grid( row = 0 , column = 0)
paper_b.grid( row = 0 , column = 1)
sciss_b.grid( row = 0 , column = 2)

window.mainloop()
