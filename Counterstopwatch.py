from tkinter import *
import time
from tkinter import messagebox

root=Tk()
root.geometry("400x300")
root.config(bg="#9d9d9d")
root.title("Timer")

hour=Entry(root,width=5,font=("Arial",20))
hour.place(x=70,y=50)
minute=Entry(root,width=5,font=("Arial",20))
minute.place(x=170,y=50)
second=Entry(root,width=5,font=("Arial",20))
second.place(x=270,y=50)

Setbtn=Button(root,font=("Arial",20),text="Set timer")
Setbtn.place(x=140,y=150)

root.mainloop()