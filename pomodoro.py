
import tkinter
from tkinter import *
from tkinter import font
import math
import plyer

FONT="Courier"
START=5
WORK_TIME=25
SHORT_BREAK=5
LONG_BREAK=10 
reps=0
timer=0

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    

def start_timer(flag):
        global timer
        min=math.floor(flag/60)
        sec=flag%60
        if(sec<10):
            sec=f"{0}{sec}"
        timer=canvas.itemconfig(timer_text,text=f"{min}:{sec}")
        
        window.after(1000,start_timer,flag-1)
        if(flag==0):
            plyer.notification.notify(title="Time for a break",message="Time is out did you finish your task?",app_name="Pomodoro Timer",app_icon="tomato.ico", timeout="5",toast=True)
            countdown()
        
def countdown():
    global reps
    reps=reps+1

    work_sec=WORK_TIME*60
    short_sec=SHORT_BREAK*60
    long_sec=LONG_BREAK*60
    if(reps%8==0):
        start_timer(long_sec)
        title_label.config(text="Long Break",fg="GREEN")
    elif(reps%2==0):
        start_timer(short_sec)
        title_label.config(text="Break",fg="GREEN")
    else:
        start_timer(work_sec)
        title_label.config(text="WORK",fg="RED")




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