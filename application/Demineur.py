from random import randint
import customtkinter as ctk
from tkinter import Frame, Button
from tkinter import ttk


def afficher_Grille(grille):
    for ligne in grille:
        for val in ligne:
            print(val,end=' ')
        print()



def creer_grille_bombe (nb_Ligne_Colone=18,nb_bombe=40):
    
    grille_bombe =[[False for _ in range(nb_Ligne_Colone)]for _ in range (nb_Ligne_Colone)]
    for i in range (nb_bombe) :
        place_bombe_c = randint(0,nb_Ligne_Colone-1)
        place_bombe_l =randint(0,nb_Ligne_Colone-1)
        #print("place_bombe_c:",place_bombe_c,"\nplace_bombe_l:",place_bombe_l)
        while grille_bombe[place_bombe_l][place_bombe_c]:
            place_bombe_c = randint(0,nb_Ligne_Colone-1)
            place_bombe_l =randint(0,nb_Ligne_Colone-1)

 
        grille_bombe[place_bombe_l][place_bombe_c]=True
    
    




app = ctk.CTk()
app.title("Prototype")
app.geometry("400x700")
app.iconbitmap("img/logo.ico")
app.resizable(width=False,height=False)
app.grid_rowconfigure(0, weight=1)  # écran principal
app.grid_rowconfigure(1, weight=0)  # barre du bas
app.grid_columnconfigure(0, weight=1)

frame_demineur = Frame(app,background="#1DD10D")
frame_demineur.grid(row=0, column=0, sticky="nsew")
frame_demineur.grid_columnconfigure(0, weight=1)

options = ["facile", "moyen", "difficile"]
choixdossier = ttk.Combobox(frame_demineur, values=options, width=50)
choixdossier.grid(row=0, column=0, padx=0, pady=0)

def on_choix(event):
    choix = choixdossier.get()
    if choix == "facile":
        creer_grille_bombe(10, 10)
        grille_joue=[['~' for _ in range(10)]for _ in range (10)]

    elif choix == "moyen":
        creer_grille_bombe(18, 40)
        grille_joue=[['~' for _ in range(18)]for _ in range (18)]

    elif choix == "difficile":
        creer_grille_bombe(24, 99)
        grille_joue=[['~' for _ in range(24)]for _ in range (24)]

choixdossier.bind("<<ComboboxSelected>>", on_choix)




app.mainloop()