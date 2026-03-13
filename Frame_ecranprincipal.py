from tkinter import *
import customtkinter as ctk

def creer_frames(app):
    

    frame_ecran1 = Frame(app)
    frame_ecran1.grid(row=0, column=0, sticky="nsew")
    
    frame_ecran2 = Frame(app, bg="#FD0000")
    frame_ecran2.grid(row=0, column=0, sticky="nsew")
    frame_ecran2.grid_remove()

    frame_verrouille = Frame(app, bg="black")
    frame_verrouille.grid(row=0, column=0, sticky="nsew")

    frame_barre = Frame(app, height=60, bg="#c1c1c1")
    frame_barre.grid(row=1, column=0, sticky="ew")
    frame_barre.grid_propagate(False)
    liste_frame = [frame_ecran1,frame_ecran2,frame_verrouille,frame_barre]


    return liste_frame

def setup_frames(liste_frame, debutswipe, finswipe, eteindretelephone, diminuerson, augmenterson, ecranaccueil):
    frame_ecran1 = liste_frame[0]
    frame_ecran2 = liste_frame[1]
    frame_verrouille = liste_frame[2]
    frame_barre = liste_frame[3]

    # swipe
    frame_ecran1.bind("<ButtonPress-1>", debutswipe)
    frame_ecran1.bind("<ButtonRelease-1>", finswipe)

    frame_ecran2.bind("<ButtonPress-1>", debutswipe)
    frame_ecran2.bind("<ButtonRelease-1>", finswipe)

    #Buttons
    buttoneteindre = ctk.CTkButton(master=frame_barre,text="Eteindre",command=eteindretelephone,width=80,height=40,border_width=0,corner_radius=4,hover=False)
    buttoneteindre.pack(side="bottom")
    buttondiminuer = ctk.CTkButton(master=frame_barre,text="",command=diminuerson,width=60,height=10,border_width=0,corner_radius=5,hover=False)
    buttondiminuer.pack(side="left",padx = 35)
    buttonprincipale = ctk.CTkButton(master=frame_barre,text="",command=ecranaccueil,width=55,height=55,border_width=0,corner_radius=30,hover=False)
    buttonprincipale.pack(side="left",padx = 42)
    buttonaugmenter = ctk.CTkButton(master=frame_barre,text="",command=augmenterson,width=60,height=60,border_width=0,corner_radius=0,hover=False)
    buttonaugmenter.pack(side="left",padx = 35)