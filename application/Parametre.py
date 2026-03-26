import customtkinter as ctk
from tkinter import *
from PIL import Image
# Changement fond d'ecran / Changement orga appli 
app = ctk.CTk()
app.title("Prototype")
app.iconbitmap("img/logo.ico")
app.geometry("400x700")
app.resizable(width=False, height=False)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
#def creer_parametre():



frame_parametre_general = Frame(app, background="#000000")
frame_parametre_general.grid(row=0, column=0, sticky="nsew")
frame_parametre_general.grid_columnconfigure(0, weight=1)
frame_parametre_general.grid_rowconfigure(0,weight=1)
frame_parametre_general.grid_rowconfigure(1,weight=0)
#frame_parametre_general.grid_remove()
frame_haut = Frame(frame_parametre_general, background="#000000")
frame_haut.grid(row=0, column=0, sticky="nsew")
frame_haut.grid_columnconfigure(0, minsize=120, weight=0)
frame_haut.grid_columnconfigure(1, minsize=280, weight=1)
frame_haut.grid_rowconfigure(0, weight=1)
frame_option = Frame(frame_haut,width=120,background="#898989")
frame_option.grid(row=0,column=0, sticky = "nsew")
frame_option.propagate(False)
frame_contenu = Frame(frame_haut, width=280, background="#2b2b2b")
frame_contenu.grid(row=0, column=1, sticky="nsew")
frame_contenu.grid_propagate(False)
frame_barre = Frame(frame_parametre_general, height=60, bg="#c1c1c1")
frame_barre.grid(row=1, column=0, sticky="ew")
frame_barre.grid_propagate(False)
frame_option = ctk.CTkScrollableFrame(frame_haut, width=120, fg_color="#898989", scrollbar_button_color="#898989", scrollbar_button_hover_color="#707070")
frame_option.grid(row=0, column=0, sticky="nsew")




frame_barre.grid_rowconfigure(0, weight=1)
frame_barre.grid_rowconfigure(1, weight=1)
frame_barre.grid_columnconfigure(0, weight=1)  
frame_barre.grid_columnconfigure(1, weight=1)  
frame_barre.grid_columnconfigure(2, weight=1)  
frame_barre.grid_columnconfigure(3, weight=1)  
buttoneteindre = ctk.CTkButton(master=frame_barre,text="Eteindre",width=80,height=40,border_width=0,corner_radius=4,hover=False)
buttoneteindre.grid(row=1, column=2, pady=2, sticky ="s")
buttondiminuer = ctk.CTkButton(master=frame_barre,text="-",width=60,height=10,fg_color="#c1c1c1",text_color="black",border_width=0,font=("Arial", 30),corner_radius=5,hover=False)
buttondiminuer.grid(row=0, column=1, padx=35, sticky ="w")
buttonprincipale = ctk.CTkButton(master=frame_barre,text="",width=55,height=55,border_width=0,corner_radius=30,hover=False)
buttonprincipale.grid(row=0, column=2, padx=42, sticky ="w")
buttonaugmenter = ctk.CTkButton(master=frame_barre,text="+",width=60,height=60,fg_color="#c1c1c1",text_color="black",border_width=0,font=("Arial", 30),corner_radius=0,hover=False)
buttonaugmenter.grid(row=0, column=3, padx=35, sticky ="w")
app.mainloop()