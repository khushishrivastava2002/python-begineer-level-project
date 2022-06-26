"""
Number Guessing Game:- 

     A number guessing game is a simple guessing game where a user is supposed to guess a number between 0 and 10, 
     you have an multiple attempts to Guess the number and as soon as you guess correctly the game with terminate automatically.
     
     
     For each wrong Guess it will give to hint that either to guess lower number or a higher number.
     
"""



# Implemetation in python

from tkinter import *
import random
from tkinter import messagebox
from tokenize import Number

#Screen
root = Tk()
root.geometry('700x500')
root.title("Number Guessing Game")
root.config(background='pink')

# Generate Number Function 
def GenerateNumberFunc():
    #Generate Number
    global Number
    Number = random.randint(1,10)
    
    # MessageBox to show that a number waas generated
    messagebox.showinfo("A Number was Generated! ","Please guess a Number")
    
# Guess Number Function

def GuessNumberFunc():
    #Get value From Answer Entry Box
    UserResponse = AnswerEntry.get()
    global Number
    # Convert values from Answer Entry Box to a number
    UserResponse = int(UserResponse)
    # CHECK IF THE user response is higher, lower or equal to that number
    if UserResponse > Number:
        ResultLabel.config(text="Incorrect! Please Guess Lower ",fg = 'red')
    elif UserResponse < Number:
        ResultLabel.config(text="Incorrect! Please Guess Higher ",fg = 'red')
    else:
        ResultLabel.config(text="You Guess Correctly! The Number was {}".format(Number),fg='green')
        AnswerEntry.delete(0)



# Title
Title = Label(root,text = "Number Guessing Game",font=("Arial",40),background='pink',foreground='purple')
Title.pack()

# Main Frame
MainFrame = Frame(root,bg="cyan",width=80,height=100)
MainFrame.pack(pady=60)

# Guess the number label
GuessNumLabel = Label(MainFrame,text = "Guess a number from 1 to 10: ",font=("Times New Roman",25),background='black',foreground='white')
GuessNumLabel.pack()

# Answer Entry
AnswerEntry = Entry(MainFrame,font=("Times New Roman",20))
AnswerEntry.pack(pady=10)

# Generate Number Button
GeneratorNumberBtn = Button(MainFrame,text='Generate Number',width=15,font=('Times New Roman',20),background='yellow',command=GenerateNumberFunc)
GeneratorNumberBtn.pack(pady=5)

# Guess Number Button
GuessBtn = Button(MainFrame,text='Guess',width=15,font=('Times New Roman',20),background='yellow',command=GuessNumberFunc)
GuessBtn.pack(pady=5)

# Result Label
ResultLabel = Label(MainFrame,text = "",font=('Times New Roman',20),background='cyan') 
ResultLabel.pack()

# Mainloop
root.mainloop()