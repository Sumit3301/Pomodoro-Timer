import tkinter
from tkinter import *
from tkinter import font

FONT="Courier"
WORK_TIME=25
SHORT_BREAK=5
LONG_BREAK=10


window=Tk()

window.title("Pomodoro")
window.config(padx=50,pady=50,bg="YELLOW")

title_label=Label(text="Timer",fg="GREEN")
title_label.grid(column=1,row=0)

canvas=Canvas(width=250,height=250)
pomodoro=PhotoImage(file="tomato.png")
canvas.create_image(120,120, image=pomodoro)
canvas.create_text(120,110,text="00:00",fill="white",font=("Arial",25,"bold"))

window.mainloop()