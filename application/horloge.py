# horloge.py
import datetime as dt
from tkinter import Frame, Label, Button, Entry
from application.Timer_class import StopWatch
from zoneinfo import ZoneInfo
from datetime import datetime

def creer_horloge(app):
    global frame_Data

    # Frame principale
    frame_horloge = Frame(app, background="#000000")
    frame_horloge.grid(row=0, column=0, sticky="nsew")
    frame_horloge.grid_remove()

    # Configurer frame_horloge pour centrer son contenu
    frame_horloge.grid_rowconfigure(0, weight=1)
    frame_horloge.grid_rowconfigure(1, weight=0)
    frame_horloge.grid_columnconfigure(0, weight=1)

    # Frame données — parent = frame_horloge 
    frame_Data = Frame(frame_horloge, background="#000000")
    frame_Data.grid(row=0, column=0)

    # Frame boutons — parent = frame_horloge 
    frame_fonctionalities = Frame(frame_horloge, background="#000000")
    frame_fonctionalities.grid(row=1, column=0, pady=10)

    # Contenu initial
    current_hour = dt.datetime.now().strftime("%H:%M:%S")
    label_welcome = Label(
        frame_Data,
        background="#000000",
        fg="white",
        font=("Calibri", 24, "bold"),
        text=f"Appli Horloge\n{current_hour}"
    )
    label_welcome.grid(row=0, column=0)

    def clear_clockapp():
        for w in frame_Data.winfo_children():
            w.destroy()

    def updateHour():
        clear_clockapp()
        label_Hour = Label(frame_Data, background="#000000", fg="white", font=("Calibri", 24, "bold"))
        label_Hour.pack()

        def refresh():
            current_time = dt.datetime.now().strftime("%H:%M:%S")
            label_Hour.config(text=current_time)
            app.after(1000, refresh)

        refresh()

    def menu_timer():
        clear_clockapp()
        timer = StopWatch(frame_Data)
        timer.pack()

        frame_button_timer = Frame(frame_Data, background='#000000')
        frame_button_timer.pack(pady=10)

        Button(frame_button_timer, text="START", bg='black', fg='white', font=("Calibri", 12), width=10, command=timer.Start).grid(row=0, column=0)
        Button(frame_button_timer, text="STOP",  bg='black', fg='white', font=("Calibri", 12), width=10, command=timer.Stop).grid(row=0, column=1)
        Button(frame_button_timer, text="RESET", bg='black', fg='white', font=("Calibri", 12), width=10, command=timer.Reset).grid(row=0, column=2)

    def world_clock():
        clear_clockapp()

        Label(frame_Data, background="#000000", fg="white", font=("Calibri", 12, "bold"),
              text='Ville exemple (Europe/Paris): ').grid(row=0, column=0)

        champ_town = Entry(frame_Data, bg="white", fg="black", font="Calibri", bd=2, justify="center")
        champ_town.grid(row=0, column=1, pady=10)

        label_town_hour = Label(frame_Data, background="#000000", fg="white", font=("Calibri", 12, "bold"))
        label_town_hour.grid(row=2, column=0)

        def display_hour():
            try:
                town = champ_town.get().strip()
                town_time = datetime.now(ZoneInfo(town))
                hour = town_time.strftime('%H:%M:%S')
                label_town_hour.config(text=f"Heure à {town.split('/')[1]} : {hour}")
            except Exception as e:
                label_town_hour.config(text='Ville invalide ou inconnue')

        Button(frame_Data, text="AFFICHER", bg='black', fg="white", font=("Calibri", 12),
               width=10, command=display_hour).grid(row=1, column=1)

    # Boutons de navigation
    Button(frame_fonctionalities, text="HEURE",  bg='black', fg="white", font=("Calibri", 12), width=10, command=updateHour).grid(row=0, column=0, padx=5)
    Button(frame_fonctionalities, text="CHRONO", bg='black', fg="white", font=("Calibri", 12), width=10, command=menu_timer).grid(row=0, column=1, padx=5)
    Button(frame_fonctionalities, text="MONDE",  bg='black', fg="white", font=("Calibri", 12), width=10, command=world_clock).grid(row=0, column=2, padx=5)

    return frame_horloge

