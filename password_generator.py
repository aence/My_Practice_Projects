# -*- coding: utf-8 -*-


import secrets

class pword:
   
   # pword class is used to create passwords
   # lists of characters to be used is specified below
   
   letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","w","q"]
   cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z', 'X', 'W', 'Q']
   nums = ["0","1","2","3","4","5","6","7","8","9"]
   puncts = [".","-","_","?","!"]
   all_letters = [*letters , *cap_letters]
   alles = [*letters , *cap_letters , *nums , *puncts]

        
   def __init__(self,length, include = ("*")):
       self.length = length
       self.include = tuple(include)
       
       # include parameter is a parameter that needed to specify which character types to be used in password
       # if not specified , include parameter gets the value of "*" in default
       # "a" for letters
       # "A" for capital letters
       # "1" for numbers
       # "-" for punctuations
       # "*" for all chararters
                    
       # creating the body of password
       chars_to_be_used = []
       for i in range(len(include)):
           if include[i] == "a":
                  chars_to_be_used.extend(pword.letters)
           if include[i] == "A":
                  chars_to_be_used.extend(pword.cap_letters)
           if include[i] == "1":
                  chars_to_be_used.extend(pword.nums)
           if include[i] == "-":
                  chars_to_be_used.extend(pword.puncts)
           if include[i] == "*":
                  chars_to_be_used.extend(pword.alles)
       new_body = []
       for i in range(0,length):
           new_body.append(secrets.choice(chars_to_be_used))
       # body of the password is created    
           
           
       self.body = new_body
               
               
               
       
   def info(self):
       
       # Gives the information (length, included characters and the amount of each character type) for the password
       
       lcount , clcount , ncount , pcount = (0,0,0,0)
       for i in range(len(self.body)):
           if self.body[i] in pword.letters:
               lcount += 1 
           if self.body[i] in pword.cap_letters:
               clcount += 1 
           if self.body[i] in pword.nums:
               ncount += 1 
           if self.body[i] in pword.puncts:
               pcount += 1 
               
       print(f"The password is {self.length} characters and includes {self.include}")
       print(f"The password contains {lcount} letters, {clcount} capital letters, {ncount} numbers, {pcount} punctuations")

   def show(self):
       
       # Shows the body of password
       
       print("Password is" + " " + "".join(self.body))
     
       
       


