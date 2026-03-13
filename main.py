import customtkinter as ctk
from tkinter import *
from img import *
# Faire que lorsque qu'on appuie une première fois sur le bouton quitter, ça éteigne l'ecran en affichant un ecran noir surement avec ctk.set_appearance_mode("dark") comme commande
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
afficher_ecran(frame_ecran1)
#tkinter
#canvas_éteint = Canvas(frame_ecran1, bg="black") 
frame_eteint = Frame(app,bg="#1c70e5")


#fill="both" : prend largeur + hauteur
#expand=True : utilise tout l’espace disponible

frame_ecran1.bind("<ButtonPress-1>", debutswipe)
frame_ecran1.bind("<ButtonRelease-1>", finswipe)
frame_ecran2.bind("<ButtonPress-1>", debutswipe)
frame_ecran2.bind("<ButtonRelease-1>", finswipe)
buttoneteindre = ctk.CTkButton(master=frame_barre,text="Eteindre",command=eteindretelephone,width=80,height=40,border_width=0,corner_radius=4,hover=False)
buttoneteindre.pack(side="bottom")
buttondiminuer = ctk.CTkButton(master=frame_barre,text="",command=diminuerson,width=60,height=10,border_width=0,corner_radius=5,hover=False)
buttondiminuer.pack(side="left",padx = 35)
buttonprincipale = ctk.CTkButton(master=frame_barre,text="",command=ecranaccueil,width=55,height=55,border_width=0,corner_radius=30,hover=False)
buttonprincipale.pack(side="left",padx = 42)
buttonaugmenter = ctk.CTkButton(master=frame_barre,text="",command=augmenterson,width=60,height=60,border_width=0,corner_radius=0,hover=False)
buttonaugmenter.pack(side="left",padx = 35)
app.mainloop()
