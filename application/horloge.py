import datetime as dt
from tkinter import *
import Timer_class


clock_app = Tk()
clock_app.title("Horloge")
clock_app.iconbitmap("img/logo.ico")
clock_app.geometry("400x640")
clock_app.config(background="#000000")

def updateHour():
    current_time = dt.datetime.now().strftime("%H:%M:%S")
    label_Hour.config(text=current_time)
    clock_app.after(1000, updateHour)


    

frame_fonctionalities = Frame(clock_app,background="#000000")
frame_fonctionalities.place(x=0,y=605)

frame_Data = Frame(clock_app,background="#000000")
frame_Data.place(relx=0.5,rely=0.5,anchor="center")

#timer = Timer_class(frame_Data)
#timer.pack()

label_Hour = Label(frame_Data,background="#000000",fg = "white",font=("Calibri", 24,"bold"))
label_Hour.pack()

button_clock = Button(frame_fonctionalities, text="HEURE", bg='black',fg="white",font=("Calibri", 12),width=10,command=updateHour)
button_clock.grid(row=0,column=0)

#button_timer = Button(frame_fonctionalities,text="CHRONOMÈTRE",bg='black',fg="white",font=("Calibri,12"),width=10,command=)
#button_timer.grid(row=0,column=1)







clock_app.mainloop()