
from random import randint
from tkinter import *
import random


root= Tk()
root.geometry("400x400")
root.title("Avi's Random Math Problems")
root.config(bg="yellow")

# variables
answer= ""
question=StringVar()
answer_variable=StringVar()
result = StringVar()
operator=["+","/","*","-"]

# Functions

def problem():
    '''
    It generate a random problem
    '''
    global answer
    sign=random.choice(operator)
    if sign=="+":
        q_1=randint(1,1000)
        q_2=randint(1,1000)
    elif sign=="*":
        q_1=randint(1,1000)
        q_2=randint(1,9)
    elif sign=="/":
        q_2=randint(1,10)
        q_1=q_2*randint(1,1000)
    elif sign=="-":
        q_2=randint(1,1000)
        q_1=randint(1,1000)
        if q_2>q_1:
            q_1,q_2=q_2,q_1
    
    question.set(str(q_1)+sign+str(q_2))
    answer_variable.set("")
    result.set("")
    
    answer=eval(question.get())
  
    
    
def check_answer():

    if answer_variable.get()=="":
        return
    
    if int(answer)==int(answer_variable.get()):
       result.set("Correct")
    else:
        result.set("Incorrect")
  
# Widgets
  
title=label=Label(text="Avi's Random Math Problems",font=("Times New Roman", 15),bg="yellow")
title.grid(row=0,column=1,columnspan=2)

generateQuestionButton=Button(text="generate question",command=problem,width=20,bg="yellow")
generateQuestionButton.grid(row=1,column=1)

entry=Entry(textvariable=question,width=20,bg="yellow")
entry.grid(row=1,column=2)

answer_label=Label(text="Enter Your Answer",width=20,bg="yellow")
answer_label.grid(row=2,column=1)

given_answer=Entry(textvariable=answer_variable,width=20,bg="yellow")
given_answer.grid(row=2,column=2)

submitAnswerButton=Button(text="submit answer",command=check_answer,width=20,bg="yellow")
submitAnswerButton.grid(row=3,column=1)

resultEntry = Entry(textvariable=result,bg="yellow")
resultEntry.grid(row=3 , column=2)


root.mainloop()