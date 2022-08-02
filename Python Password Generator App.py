# -*- coding: utf-8 -*-


import tkinter as tk
import password_generator as pw

window = tk.Tk()
window.title("Python Password Generator App")
window.geometry("450x300")

    
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()

include = []

label_1 = tk.Label( text= "Length")
label_2 = tk.Label( text= "Password")
info_label = tk.Label( text = "Welcome to password generator app! \n Type the length of your password and select the characters to be included.", height = 4)


length = tk.Entry( width = 3 , font = ("Helvetica")  , relief = tk.SUNKEN , borderwidth = 5 )
password_window = tk.Entry( width = 25 , font = ("Helvetica")  , relief = tk.SUNKEN , borderwidth = 5 )

letter_check = tk.Checkbutton(text = "Letters" , variable = var1 , command = lambda : adder(var1,"a"))
cap_letter_check = tk.Checkbutton(text = "Capital Letters" , variable = var2 , command = lambda : adder(var2,"A"))
num_check = tk.Checkbutton(text = "Numbers" , variable = var3 , command = lambda : adder(var3,"1"))
punc_check = tk.Checkbutton(text = "Punctuations" , variable = var4 , command = lambda : adder(var4,"-"))
all_check = tk.Checkbutton(text = "All Characters" , variable = var5 , command = lambda : adder(var5,"*"))


create_button = tk.Button( text ="Create Password" , bg = "#fcdf03" , command = lambda : generate(int(length.get()),tuple(include),password_window) )


def adder(a,b):
    if a.get() == 1 :
        global include
        include.append(b)
    elif a.get() == 0:
        include.remove(b)
        
#    print(include)
        
def generate(length_input,include,password_window):
    
    k = pw.pword(int(length_input), tuple(include))
    password_window.delete(0,int(length_input))
    password_window.insert(0,"".join(k.body))

        
        









label_1.grid(row = 1 , column = 0 , sticky = "W")
label_2.grid(row = 7 , column = 0 , sticky = "W")
info_label.grid(row = 0 , columnspan = 4 , sticky = "WENS")
length.grid(row = 1 , column = 1 , sticky = "W")
letter_check.grid(row = 2 , column = 1 , sticky = "W")
cap_letter_check.grid(row = 3 , column = 1 , sticky = "W")
num_check.grid(row = 4 , column = 1 , sticky = "W")
punc_check.grid(row = 5 , column = 1 , sticky = "W")
all_check.grid(row = 6 , column = 1 , sticky = "W")
create_button.grid(row = 4, column = 3)
password_window.grid(row = 7 , column = 1 , sticky = "WENS")












window.mainloop()