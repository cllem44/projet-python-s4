from tkinter import *
import time
import geocoder
import tkintermapview as tkm


def get_position():
    g = geocoder.ip('me')
    return g.latlng

def update_position():
    latlng = get_position()
    if latlng:
        label_latitude.config(text=f'Votre latitude: {latlng[0]}')
        label_longitude.config(text=f'Votre longitude: {latlng[1]}')
    map_app.after(1000,update_position)

map_app = Tk()
map_app.title("Horloge")
map_app.iconbitmap("img/logo.ico")
map_app.geometry("400x640")
map_app.config(background="#000000")


frame_latlng = Frame(map_app,background="#000000")
frame_latlng.pack(anchor='n')

label_latitude = Label(frame_latlng,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
label_latitude.grid(row=0,column=0)

label_longitude = Label(frame_latlng,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
label_longitude.grid(row=1,column=0)


update_position()

map_widget = tkm.TkinterMapView(map_app,width=400,height=500,corner_radius=0)
map_widget.set_position(48.860381, 2.338594)  # Paris, France
map_widget.set_zoom(15)
map_widget.pack()

map_app.mainloop()