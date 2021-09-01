import tkinter
from tkinter import *
from tkinter import font
import time

FONT="Courier"
WORK_TIME=25
SHORT_BREAK=5
LONG_BREAK=10 

def countdown(flag):
    canvas.itemconfig(timer_text,text=flag)
    while(flag>0):
        window.after(1000,countdown,flag-1)

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
countdown(60)
start=Button(text="Start")
start.grid(column=0,row=3)

reset=Button(text="reset")
reset.grid(column=3,row=3)


#countdown mechanism

         

window.mainloop()