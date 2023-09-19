import random
from tkinter import *

schema={
    "rock":{"rock":1,"paper":0,"scissor":2},
    "paper":{"rock":2,"paper":1,"scissor":0},
    "scissor":{"rock":0,"paper":2,"scissor":1}
}
comp_score=0
player_score=0


def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes=["rock","paper","scissor"]
    random_number=random.randint(0,2)
    computer_choice=outcomes[random_number]
    result=schema[user_choice][computer_choice]

    player_choice_label.config(fg="red",text="Player Choice: "+str(user_choice))
    computer_choice_label.config(fg="green",text="Computer Choice: "+str(computer_choice))
    
    if result==2:
        player_score=player_score+1
        player_score_label.config(text="player:"+str(player_score))
        outcome_label.config(fg="blue",text="Outcome:Player won")
    elif result==1:
        player_score=player_score+0
        comp_score=player_score+0
        player_score_label.config(text="player:"+str(player_score))
        computer_score_label.config(text="computer:"+str(comp_score))
        outcome_label.config(fg="blue",text="Outcome:Draw")
    elif result==0:
        comp_score=comp_score+1
        computer_score_label.config(text="computer:"+str(comp_score))
        outcome_label.config(fg="blue",text="Outcome:Computer won")




master=Tk()
master.title("RPS")

Label(master,text="Rock,Paper,Scissor",font=("Calibri,15"),fg="orange").grid(row=0,column=1,pady=10,padx=200)
Label(master,text="Please select an option",font=("Calibri,14")).grid(row=1,column=1)
player_score_label=Label(master,text="Player:0",font=("Calibri",13),bg="grey",fg="white")
player_score_label.grid(row=2,column=0)
computer_score_label=Label(master,text="Computer:0",font=("Calibri",13),bg="grey",fg="white")
computer_score_label.grid(row=2,column=2)
player_choice_label=Label(master,font=("Calibri",13))
player_choice_label.grid(row=3,column=0)
computer_choice_label=Label(master,font=("Calibri",13))
computer_choice_label.grid(row=3,column=2) 
outcome_label=Label(master,font=("Calibri",13))
outcome_label.grid(row=3,column=1)



Button(master,text="Rock",width=15,command=lambda:outcome_handler("rock"),bg="yellow",fg="red").grid(row=4,column=0,padx=7,pady=7)
Button(master,text="Paper",width=15,command=lambda:outcome_handler("paper"),bg="yellow",fg="red").grid(row=4,column=1,pady=7,padx=7)
Button(master,text="Scissor",width=15,command=lambda:outcome_handler("scissor"),bg="yellow",fg="red").grid(row=4,column=2,padx=7,pady=7)



Label(master).grid(row=5)
master.mainloop()