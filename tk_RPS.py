import tkinter as kt
from tkinter import ttk as ktk
import random as ran
from tkinter.messagebox import showinfo
root = kt.Tk()

main = kt.Frame(root)
main.pack()

def return_result(result):
    showinfo(title="Result", message=result)
    
def compare_result(user_input):
    ran_input = ran.randrange(0,3)
    if (user_input == 0):
        if (ran_input == 0):
            result = "Tied! Both are rock!"
        elif (user_input == 0 & ran_input == 1):
            result = "Paper beats rock, sorry!"
        elif (ran_input == 2):
            result = "Rock beats scissors, congrats!"
    elif (user_input == 1):
        if (ran_input == 0):
            result = "Paper beats rock, congrats!"
        elif (ran_input == 1):
            result = "Tied! Both are paper!"
        elif (ran_input == 2):
            result = "Scissors beats paper, sorry!"
    elif (user_input == 2):
        if (ran_input == 0):
            result = "Rock beats scissors, sorry!"
        elif (ran_input == 1):
            result = "Scissors beats paper, congrats!"
        elif (ran_input == 2):
            result = "Tied! Both are scissors!"
    else:
        result = "Wrong input!"
    return_result(result);

title = ktk.Label(main, text="Rock, Paper, Scissors")
btn_rock  = ktk.Button(main, text="Rock (0)", command=lambda: compare_result(0))
btn_rock.pack()
btn_paper = ktk.Button(main, text="Paper (1)", command=lambda: compare_result(1))
btn_paper.pack()
btn_scissors = ktk.Button(main, text="Scissors (2)", command=lambda: compare_result(2))
btn_scissors.pack()
btn_playAgain = ktk.Button(main, text="Play Again?")
btn_playAgain.pack()

root.mainloop()

