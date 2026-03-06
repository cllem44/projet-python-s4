import customtkinter as ctk
from tkinter import *
# Faire que lorsque qu'on appuie une première fois sur le bouton quitter, ça éteigne l'ecran en affichant un ecran noir surement avec ctk.set_appearance_mode("dark") comme commande

def Eteindretelephone():
    canvas.pack(fill="both", expand=True)

def Ecranaccueil():
    canvas.pack_forget()
#customtkinter
app = ctk.CTk()
app.title("Prototype")
app.geometry("400x700")
app.resizable(width=False,height=False)
frame_ecran = Frame(app)
frame_ecran.pack(fill="both", expand=True)
barre_bas = Frame(app, height=60, bg="#c1c1c1")
barre_bas.pack(fill="x", side="bottom")
#tkinter
canvas = Canvas(frame_ecran, bg="black") 
#fill="both" : prend largeur + hauteur
#expand=True : utilise tout l’espace disponible

buttoneteindre = ctk.CTkButton(master=barre_bas,text="Eteindre",command=Eteindretelephone,width=80,height=40,border_width=0,corner_radius=4,hover=False)
buttoneteindre.pack(side="bottom")
buttonprincipale = ctk.CTkButton(master=barre_bas,text="",command=Ecranaccueil,width=55,height=55,border_width=0,corner_radius=30,hover=False)
buttonprincipale.pack(side="bottom")
app.mainloop()