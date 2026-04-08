from tkinter import *
import customtkinter as ctk
from PIL import Image

def creer_frames(app):
    global liste_frame

    frame_ecran1 = Frame(app)
    frame_ecran1.grid(row=0, column=0, sticky="nsew")

    frame_ecran2 = Frame(app, bg="#FD0000")
    frame_ecran2.grid(row=0, column=0, sticky="nsew")
    frame_ecran2.grid_remove()

    frame_verrouille = Frame(app, bg="black")
    frame_verrouille.grid(row=0, column=0, sticky="nsew")
    frame_verrouille.grid_remove()

    frame_barre = Frame(app, height=60, bg="#c1c1c1")
    frame_barre.grid(row=1, column=0, sticky="ew")



    liste_frame = [frame_ecran1,frame_ecran2,frame_verrouille,frame_barre]
    return liste_frame

def charger_image(url):
    image = ctk.CTkImage(light_image=Image.open(url), size= (50,50))
    return image

def setup_frames(frame_barre, eteindretelephone, diminuerson, augmenterson, ecranaccueil):
    frame_barre.columnconfigure((0,1,2,3,4,5), weight=1)
    frame_barre.rowconfigure(0, weight=1)
    frame_barre.rowconfigure(1, weight=1)
    
    #Buttons
    buttoneteindre = ctk.CTkButton(master=frame_barre,text="Eteindre",command=eteindretelephone,width=80,height=40,fg_color="#c1c1c1",text_color="black",border_width=0,corner_radius=4,hover=False)
    buttoneteindre.grid(row=1, column=2, pady=2, sticky ="s")
    
    buttondiminuer = ctk.CTkButton(master=frame_barre,text="-",command=diminuerson,width=60,height=10,fg_color="#c1c1c1",text_color="black",border_width=0,font=("Arial", 30),corner_radius=5,hover=False)
    buttondiminuer.grid(row=0, column=1, padx=35, sticky ="w")
    
    buttonprincipale = ctk.CTkButton(master=frame_barre,text="⬤",command=ecranaccueil,width=155,height=55,fg_color="#c1c1c1",text_color="black",border_width=0,font=("Arial", 60),corner_radius=30,hover=False)
    buttonprincipale.grid(row=0, column=2, padx=42, sticky ="w")
    
    buttonaugmenter = ctk.CTkButton(master=frame_barre,text="+",command=augmenterson,width=60,height=60,fg_color="#c1c1c1",text_color="black",border_width=0,font=("Arial", 30),corner_radius=0,hover=False)
    buttonaugmenter.grid(row=0, column=3, padx=35, sticky ="w")

def placer_app(frame,icone,lancerapp,ligne,colonne):
    frame.columnconfigure((0,1,2,3), weight=1)
    frame.rowconfigure((0,1,2,3), weight=1)

    #Applications
    buttonapp = ctk.CTkButton(master=frame,image=icone,text="",command=lancerapp,width=50,height=50,fg_color="transparent",bg_color="transparent",border_width=0,corner_radius=0,hover=False)
    buttonapp.grid(row=ligne,column=colonne,padx=10,pady=10,sticky="w")
