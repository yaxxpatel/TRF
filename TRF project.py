# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 18:22:56 2023

@author: admin
"""

from tkinter import *
import random

root=Tk()
root.title("TESTING RANDOM FUNCTION")
root.geometry("600x500")

label = Label(root)
input_password = input(root)
guessed_password_label = Label(root)
guessed_password_label["text"] = "Guessed Password : " + input_password.get()

array_3d = [[["A","B","C","D","M","N","O","P"],["Alien","Human"],["!","@","#","$","%","^","&","*"]]]
print(array_3d[0][1][1])

def new_password():
    random_no_1 = random.randint(0,7)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,7)
    
    letter_1 = str(array_3d[0][0][random_no_1])
    letter_2 = (array_3d[0][1][random_no_2])
    letter_3 = (array_3d[0][2][random_no_3])
    label["text"] = letter_1 + "" + letter_2 + "" + letter_3
    
btn = Button(root, text = "New Password", command = new_password)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
input_password.place(relx = 0.5, rely = 0.3, anchor = CENTER)
guesses_password_label.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()