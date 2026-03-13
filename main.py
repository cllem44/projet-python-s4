import customtkinter as ctk
from tkinter import *
from img import *
from PIL import ImageTk,Image
from Frame_ecranprincipal import *
# Faire 1 frame par app a chaque fois 

debut_x = 0
debut_y = 0

def afficher_ecran(frame):
    for f in (frame_ecran1, frame_ecran2, frame_verrouille):
        f.grid_remove()
    frame.grid()

def eteindretelephone():
    afficher_ecran(frame_verrouille)

def ecranaccueil():
    afficher_ecran(frame_ecran1)

def debutswipe(event):
    global debut_x, debut_y
    debut_x = event.x
    debut_y = event.y

def finswipe(event):
    dx = event.x - debut_x
    dy = event.y - debut_y
    if abs(dx) > abs(dy):
        if dx < 20:
            afficher_ecran(frame_ecran2)
        elif dx > -20:
            afficher_ecran(frame_ecran1)

# Si on veut faire un menu déroulant ou quelques choses du style vers le bas ou le haut 
            """
    else:
        if dy > 20:
            #Swipe bas
        elif dy < -20:
            #Swipe haut
"""
def diminuerson():
    pass

def augmenterson():
    pass


#customtkinter
app = ctk.CTk()
app.title("Prototype")
app.geometry("400x700")
app.iconbitmap("img/logo.ico")
app.resizable(width=False,height=False)
app.grid_rowconfigure(0, weight=1)  # écran principal
app.grid_rowconfigure(1, weight=0)  # barre du bas
app.grid_columnconfigure(0, weight=1)

# FRAMES 
frame_ecran1, frame_ecran2, frame_verrouille, frame_barre = creer_frames(app)
frames = [frame_ecran1, frame_ecran2, frame_verrouille, frame_barre]
setup_frames(frames,debutswipe,finswipe,eteindretelephone,diminuerson,augmenterson,ecranaccueil)
afficher_ecran(frame_ecran1)

app.mainloop()
