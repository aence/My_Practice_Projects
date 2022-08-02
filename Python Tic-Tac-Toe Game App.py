# -*- coding: utf-8 -*-


import tkinter as tk

#Creating the main window

window = tk.Tk()
window.title("Python Tic Tac Toe Game App")
window.geometry("350x270")

#Setting parameters to the app

h = 4
w = 2*h
t = " "
tour = 0
value = "X"
winner = False

#Creating the necessary widgets

frame_1 = tk.Frame()
table_title = tk.Label(text = "Playing Table" , borderwidth = 1,  font = ("Helvetica",  "12"))
player_title = tk.Label(text = f"Current player is {value}" , font = ("Helvetica",  "12"),borderwidth = 1)
winner_title = tk.Label(text = "Who will win?" , font = ("Helvetica",  "12"))

button_1 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_1,value))
button_2 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_2,value))
button_3 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_3,value))
button_4 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_4,value))
button_5 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_5,value))
button_6 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_6,value))
button_7 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_7,value))
button_8 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_8,value))
button_9 = tk.Button(master = frame_1 , text = t, width = w , height = h , bg = "#f7f6b0" , relief = "sunken" ,  command = lambda: insert(button_9,value))

#Setting the geometry of the widgets                     
                     
frame_1.grid(row = 1 , column = 0)
table_title.grid(row = 0 , column = 0)
player_title.grid(row = 1 , column = 1 , sticky = "N" )
winner_title.grid(row = 1 , column = 1 , sticky = "S")
button_1.grid(row = 0 , column = 0 , sticky = "WENS")
button_2.grid(row = 0 , column = 1 , sticky = "WENS")
button_3.grid(row = 0 , column = 2 , sticky = "WENS")
button_4.grid(row = 1 , column = 0 , sticky = "WENS")
button_5.grid(row = 1 , column = 1 , sticky = "WENS")
button_6.grid(row = 1 , column = 2 , sticky = "WENS")
button_7.grid(row = 2 , column = 0 , sticky = "WENS")
button_8.grid(row = 2 , column = 1 , sticky = "WENS")
button_9.grid(row = 2 , column = 2 , sticky = "WENS")

# Setting the function to control the winning conditions
    
def control():
    global winner
    
    if (button_1["text"] == button_2["text"] == button_3["text"] == "X") or (button_1["text"] == button_2["text"] == button_3["text"] == "O") :
       winner_title["text"] = f"Winner is {value}"
       winner = True
    elif (button_4["text"] == button_5["text"] == button_6["text"] == "X") or (button_4["text"] == button_5["text"] == button_6["text"] == "O") :
        winner_title["text"] = f"Winner is {value}"
        winner = True
    elif (button_7["text"] == button_8["text"] == button_9["text"] == "X") or (button_7["text"] == button_8["text"] == button_9["text"] == "O") :
        winner_title["text"] = f"Winner is {value}"
        winner = True
    elif (button_1["text"] == button_4["text"] == button_7["text"] == "X") or (button_1["text"] == button_4["text"] == button_7["text"] == "O") :
       winner_title["text"] = f"Winner is {value}"
       winner = True
    elif (button_2["text"] == button_5["text"] == button_8["text"] == "X") or (button_2["text"] == button_5["text"] == button_8["text"] == "O") :
       winner_title["text"] = f"Winner is {value}"
       winner = True
    elif (button_3["text"] == button_6["text"] == button_9["text"] == "X") or (button_3["text"] == button_6["text"] == button_9["text"] == "O") :
       winner_title["text"] = f"Winner is {value}"
       winner = True
    elif (button_1["text"] == button_5["text"] == button_9["text"] == "X") or (button_1["text"] == button_5["text"] == button_9["text"] == "O") :
       winner_title["text"] = f"Winner is {value}"
       winner = True
    elif (button_3["text"] == button_5["text"] == button_7["text"] == "X") or (button_3["text"] == button_5["text"] == button_7["text"] == "O") :
       winner_title["text"] = f"Winner is {value}"
       winner = True
    elif button_1["bg"] != "#f7f6b0" and button_2["bg"] != "#f7f6b0"  and button_2["bg"] != "#f7f6b0" and button_3["bg"] != "#f7f6b0" and button_4["bg"] != "#f7f6b0" and button_5["bg"] != "#f7f6b0" and button_6["bg"] != "#f7f6b0" and button_7["bg"] != "#f7f6b0" and button_8["bg"] != "#f7f6b0" and button_9["bg"] != "#f7f6b0":
        winner_title["text"] = "Draw"
        winner = True
    
#Setting the function to be called to insert a value inside a square
        
def insert(button,x_or_o):
    global value
    global tour
    global winner
    
    if winner ==  False and button["bg"] == "#f7f6b0":
        if tour % 2 == 1:
            value = "O"
        else:
            value = "X"
    
        button["text"] = value
        
       
        if value == "X":
            button["bg"] = "#ebe834"
            player_title["text"] ="Current player is O"
        elif value == "O":
            button["bg"] = "#ebb734"
            player_title["text"] ="Current player is X"
            
        control()
        
        tour +=1 
    else:
        pass
    
    
    
    
    







window.mainloop()


        


