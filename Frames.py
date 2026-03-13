from tkinter import *


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