#pip install tzdata
import datetime as dt
from tkinter import *
from Timer_class import *
from zoneinfo import ZoneInfo
from datetime import datetime


clock_app = Tk()
clock_app.title("Horloge")
clock_app.iconbitmap("img/logo.ico")
clock_app.geometry("400x640")
clock_app.config(background="#000000")

def world_clock():
    clear_clockapp()

    label_town = Label(frame_Data,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
    label_town.config(text='Ville souhaitée (Continent/Ville): ')
    label_town.grid(row=0,column=0)

    champ_town = Entry(frame_Data, bg="white", fg="black",font="Calibri", bd=2, justify=CENTER)
    champ_town.grid(row=0,column=1)
    
    label_town_hour = Label(frame_Data,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
    label_town_hour.grid(row=1,column=0)

    def display_hour():
        try:
            town = champ_town.get().strip()

            town_time = datetime.now(ZoneInfo(town))
            hour = town_time.strftime('%H:%M:%S')

            label_town_hour.config(text=f'Heure à {town.split('/')[1]} : {hour}')
        
        except Exception as e:
            print(e)
            label_town_hour.config(text='Ville invalide ou inconnue')
    
    button_world_hour = Button(frame_fonctionalities,text = "AFFICHER",bg='black',fg="white",font=("Calibri",12),width=10,command=display_hour)
    button_world_hour.grid(row=0,column=3)

    
    



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

label_welcome = Label(frame_Data,background="#000000",fg = "white",font=("Calibri", 24,"bold"))
label_welcome.config(text="Bienvenue dans l'app horloge")
label_welcome.grid(row=0,column=0)


button_clock = Button(frame_fonctionalities, text="HEURE", bg='black',fg="white",font=("Calibri",12),width=10,command=updateHour)
button_clock.grid(row=0,column=0)


button_timer = Button(frame_fonctionalities,text="CHRONO",bg='black',fg="white",font=("Calibri",12),width=10,command=menu_timer)
button_timer.grid(row=0,column=1)

button_world_clock = Button(frame_fonctionalities,text="MONDE",bg='black',fg="white",font=("Calibri",12),width=10,command=world_clock)
button_world_clock.grid(row=0,column=2)






clock_app.mainloop()