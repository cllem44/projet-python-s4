import datetime as dt
from tkinter import *
from Timer_class import *


clock_app = Tk()
clock_app.title("Horloge")
clock_app.iconbitmap("img/logo.ico")
clock_app.geometry("400x640")
clock_app.config(background="#000000")

def clear_clockapp():
    for w in frame_Data.winfo_children():
        w.destroy()



def updateHour():
    clear_clockapp()

    global label_Hour
    label_Hour = Label(frame_Data,background="#000000",fg = "white",font=("Calibri", 24,"bold"))
    label_Hour.pack()
    
    def refresh():
        current_time = dt.datetime.now().strftime("%H:%M:%S")
        label_Hour.config(text=current_time)
        clock_app.after(1000, refresh)

    refresh()


def menu_timer():

    clear_clockapp()
    timer = StopWatch(frame_Data)
    timer.pack()

    frame_button_timer = Frame(frame_Data,background='#000000')
    frame_button_timer.pack(pady=10)

    button_start = Button(frame_button_timer,text="START",bg='black',fg='white',font=("Calibri",12),width=10,command=timer.Start)
    button_stop = Button(frame_button_timer,text="STOP",bg='black',fg='white',font=("Calibri",12),width=10,command=timer.Stop)
    button_reset = Button(frame_button_timer,text="RESET",bg='black',fg='white',font=("Calibri",12),width=10,command=timer.Reset)
    button_start.grid(row=0,column=0)
    button_stop.grid(row=0,column=1)
    button_reset.grid(row=0,column=2)


    


    

frame_fonctionalities = Frame(clock_app,background="#000000")
frame_fonctionalities.place(x=0,y=605)

frame_Data = Frame(clock_app,background="#000000")
frame_Data.place(relx=0.5,rely=0.5,anchor="center")


button_clock = Button(frame_fonctionalities, text="HEURE", bg='black',fg="white",font=("Calibri",12),width=10,command=updateHour)
button_clock.grid(row=0,column=0)


button_timer = Button(frame_fonctionalities,text="CHRONO",bg='black',fg="white",font=("Calibri",12),width=10,command=menu_timer)
button_timer.grid(row=0,column=1)

#button_world_clock = Button(frame_fonctionalities,text="MONDE",bg='black',fg="white",font=("Calibri",12),width=10,command=)
#button_world_clock.grid(row=0,column=2)






clock_app.mainloop()