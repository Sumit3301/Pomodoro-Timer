import tkinter
from tkinter import *
from tkinter import font
import time
import math
import plyer

FONT="Courier"
START=5
WORK_TIME=25
SHORT_BREAK=5
LONG_BREAK=10 
global reps



def reset():
    canvas.itemconfig(timer_text,text=f"{00}:{00}")
    reps=0

def start_timer(flag):
        min=math.floor(flag/60)
        sec=flag%60
        if(sec<10):
            sec=f"0{sec}"
            canvas.itemconfig(timer_text,text=f"{min}:{sec}")
            window.after(1000,start_timer,flag-1)

        if(flag<0):
            plyer.notification.notify(title="Time for a break",message="Time is out did you finish your task?",app_name="Pomodoro Timer",app_icon="tomato.ico", timeout="5",toast=True) 

def countdown():
    reps=0
    while(reps<5):
        start_timer(START)
        time.sleep(1)
        start_timer(WORK_TIME)
        time.sleep(1)
        start_timer(SHORT_BREAK)
        reps+=1

window=Tk()

window.title("Pomodoro")
window.config(padx=50,pady=50,bg="YELLOW")

title_label=Label(text="Timer",fg="GREEN",bg="YELLOW")
window.iconbitmap('tomato.ico')

title_label.grid(column=1,row=0)
title_label.config(font=('Helvatical bold',40))


canvas=Canvas(width=250,height=250)
pomodoro=PhotoImage(file="tomato.png")
canvas.create_image(120,120, image=pomodoro)
timer_text=canvas.create_text(120,110,text="00:00",fill="white",font=("Arial",25,"bold"))
canvas.grid(column=1,row=2)



start=Button(text="Start",command=countdown)
start.grid(column=0,row=3)

reset=Button(text="reset",command=reset)
reset.grid(column=3,row=3)


         

window.mainloop()