#pip install geocoder
#pip install tkintermapview
from tkinter import *
import time
import geocoder
import tkintermapview as tkm

def creer_map():
    #acquiert la position de l'utilisateur à partir de son adresse ip
    def get_position():
        g = geocoder.ip('me')
        return g.latlng

    #rafraîchit la position de l'utilisateur toutes les secondes
    def update_position():
        global latlng
        latlng = get_position()
        if latlng:
            label_latitude.config(text=f'Votre latitude: {latlng[0]}')
            label_longitude.config(text=f'Votre longitude: {latlng[1]}')
        map_app.after(1000,update_position)

    #Ajoute les nouveaux markers et les relie entre eux en partant de la position départ
    def add_marker_path(coords):
        global list_coord,path_1

        list_coord.append((coords[0],coords[1]))
        map_widget.set_marker(coords[0],coords[1],text="Nouveau point")

        if path_1:
            path_1.delete()

        path_1 = map_widget.set_path(list_coord,color='blue',width=2)


    #Définit l'évènement effectué pour un clic gauche sur la carte
    def left_click_event(coordinates_tuple):
        print("Coordonnées du lieu clické:", coordinates_tuple)
        


    map_app = Tk()
    map_app.title("MAP")
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
    list_coord = [(latlng[0],latlng[1])]
    path_1=None

    map_widget = tkm.TkinterMapView(frame_latlng,width=400,height=500,corner_radius=0)
    map_widget.set_position(latlng[0],latlng[1],marker=True)
    map_widget.set_zoom(15)
    map_widget.add_right_click_menu_command(label="Ajouter position",command=add_marker_path,pass_coords=True,)
    map_widget.add_right_click_menu_command(label= "Supprimer position(s)",command=map_widget.delete_all_marker)
    map_widget.add_right_click_menu_command(label="Suppimer chemin(s)",command=map_widget.delete_all_path)
    map_widget.add_left_click_map_command(left_click_event)
    map_widget.grid(row=2,column=0)

    map_app.mainloop()