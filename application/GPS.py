#pip install geocoder
#pip install tkintermapview
from tkinter import *
import time
import geocoder
import tkintermapview as tkm
import math

def creer_map(app):
    global list_coord
    #acquiert la position de l'utilisateur à partir de son adresse ip(pas très précis)
    def get_position():
        g = geocoder.ip('me')
        return g.latlng

    #rafraîchit la position de l'utilisateur toutes les Minutes
    def update_position():
        global ltlng        
        ltlng = get_position()

        if ltlng is None:
            ltlng = (48.8566,2.3522)
            label_latitude.config(text=f'Votre latitude: {ltlng[0]}')
            label_longitude.config(text=f'Votre longitude: {ltlng[1]}')
        else:
            label_latitude.config(text=f'Votre latitude: {ltlng[0]}')
            label_longitude.config(text=f'Votre longitude: {ltlng[1]}')
        
        app.after(60000,update_position)

    #Permet de calculer la distance entre les deux derniers points placés grâce à la loi des sinus
    def distance_last_point(list_coord):
        if len(list_coord)<2:
            return 0
        
        r = 6371
        lat1 = list_coord[-2][0]
        lng1 = list_coord[-2][1]
        lat2 = list_coord[-1][0]
        lng2 = list_coord[-1][1]

        lat1,lng1 = math.radians(lat1),math.radians(lng1)
        lat2,lng2 = math.radians(lat2),math.radians(lng2)

        d = r*math.acos(math.sin(lat1)*math.sin(lat2)+math.cos(lat1)*math.cos(lat2)*math.cos(lng2-lng1))
        return d

    #Ajoute les nouveaux markers et les relie entre eux en partant de la position départ
    def add_marker_path(coords):
        nonlocal path_1
        global list_coord
        
        
        list_coord.append((coords[0],coords[1]))
        map_widget.set_marker(coords[0],coords[1],text="Nouveau point")

        if path_1:
            path_1.delete()

        path_1 = map_widget.set_path(list_coord,color='blue',width=2)

    #Définit l'évènement effectué pour un clic gauche sur la carte
    def left_click_event(coordinates_tuple):
        pass
        #print("Coordonnées du lieu clické:", coordinates_tuple)
    
    def display_distance():
        label_latitude.config(text='')
        label_longitude.config(text='')
        label_latitude.config(text=f'Distance deux derniers points : {distance_last_point(list_coord)} km')

    def delete_marker():
        global list_coord

        map_widget.delete_all_marker()
        list_coord = [(ltlng[0],ltlng[1])]
        map_widget.set_marker(list_coord[0][0],list_coord[0][1],text="Départ")

       


    '''map_app = Tk()
    map_app.title("MAP")
    map_app.iconbitmap("img/logo.ico")
    map_app.geometry("400x640")
    map_app.config(background="#000000")'''

    #Initialisation de la frame et des labels
    frame_latlng = Frame(app,background="#000000")
    frame_latlng.grid(row=0, column=0, sticky="nsew")
    frame_latlng.grid_propagate(False)

    frame_latlng.grid_columnconfigure(0, weight=1)
    frame_latlng.grid_rowconfigure(0, weight=0)  # latitude
    frame_latlng.grid_rowconfigure(1, weight=0)  # longitude
    frame_latlng.grid_rowconfigure(2, weight=1)
                                   
    label_latitude = Label(frame_latlng,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
    label_latitude.grid(row=0,column=0,sticky="ew")

    label_longitude = Label(frame_latlng,background="#000000",fg = "white",font=("Calibri", 12,"bold"))
    label_longitude.grid(row=1,column=0,sticky="ew")

    path_1=None
    update_position()
    list_coord = [(ltlng[0],ltlng[1])]
    
    #Création de la carte et placement sur la frame, réglages du menu click droit et 
    map_widget = tkm.TkinterMapView(frame_latlng,width=400,height=500,corner_radius=0)
    map_widget.set_position(ltlng[0],ltlng[1],marker=True)
    map_widget.set_zoom(15)
    map_widget.add_right_click_menu_command(label="Ajouter position",command=add_marker_path,pass_coords=True,)
    map_widget.add_right_click_menu_command(label= "Supprimer position(s)",command=delete_marker)
    map_widget.add_right_click_menu_command(label="Suppimer chemin(s)",command=map_widget.delete_all_path)
    map_widget.add_right_click_menu_command(label="Distance 2 derniers points",command=display_distance)
    map_widget.add_left_click_map_command(left_click_event)
    map_widget.grid(row=2,column=0, sticky="nsew")

    return frame_latlng

#creer_map()