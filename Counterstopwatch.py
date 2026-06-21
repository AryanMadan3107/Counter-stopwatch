from tkinter import *
import time
from tkinter import messagebox

root=Tk()
root.geometry("400x300")
root.config(bg="#9d9d9d")
root.title("Timer")

def countdown():

    hourentry.config(state="disabled")
    minuteentry.config(state="disabled")
    secondentry.config(state="disabled")
    setbtn.config(state="disabled")

    h=int(hourentry.get())
    m=int(minuteentry.get())
    s=int(secondentry.get())
    temp=h*3600+m*60+s
    while temp>=0:
        min,sec=divmod(temp,60)
        if min>60:
            hr,min=divmod(min,60)
        else:
            hr=0
        hour.set("{:02d}".format(hr))
        minute.set("{:02d}".format(min))
        second.set("{:02d}".format(sec))
        root.update()
        time.sleep(1)
        temp-=1
        if temp==0:
            messagebox.showinfo("Countdown","Time's up!")


hour=StringVar()
hour.set("00")

minute=StringVar()
minute.set("00")

second=StringVar()
second.set("00")

hourentry=Entry(root,width=5,font=("Arial",20),textvariable=hour)
hourentry.place(x=70,y=50)
minuteentry=Entry(root,width=5,font=("Arial",20),textvariable=minute)
minuteentry.place(x=170,y=50)
secondentry=Entry(root,width=5,font=("Arial",20),textvariable=second)
secondentry.place(x=270,y=50)

setbtn=Button(root,font=("Arial",20),text="Set timer", command=countdown)
setbtn.place(x=140,y=150)

root.mainloop()