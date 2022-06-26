import random
from tkinter import Button, Label
from tkinter import *

# min = 1
# max = 6

root = Tk()
root.geometry('700x450')
root.title("Dice Simulator")
root.config(background= 'pink')
l1 = Label(root,font=("times",200))

def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(background ='purple',text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1 = Button(root,text="lets roll...",command=roll)
b1.place(x = 330,y = 0)
# roll_again = "yes"

# while roll_again == "yes" or roll_again == 'y':
#     print("Rolling the dice... ")
#     print("This Values are...")
#     print(random.randint(min,max))
#     roll_again = input("Do you what to Roll the dices Again?  y/n  or  yes/no \n")
#     roll_again = roll_again.lower()

root.mainloop()