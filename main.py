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

#tkinter
canvas = Canvas(app, bg="black") 
#fill="both" : prend largeur + hauteur
#expand=True : utilise tout l’espace disponible

app.create_rectangle(0,600,400,600,fill="#c1c1c1")
buttoneteindre = ctk.CTkButton(master=app,text="Eteindre",command=Eteindretelephone,width=80,height=40,border_width=0,corner_radius=4,hover=False)
buttoneteindre.pack(side="bottom")
buttonprincipale = ctk.CTkButton(master=app,text="",command=Ecranaccueil,width=55,height=55,border_width=0,corner_radius=30,hover=False)
buttonprincipale.pack(side="bottom")
app.mainloop()