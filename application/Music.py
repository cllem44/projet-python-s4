import customtkinter as ctk
from tkinter import *
import PIL.Image as PilImage
from PIL import Image

def play():
    print("caca")

def pause():
    print("pdssd")

def retour():
    print("ttt")

def suivant():
    print("dsd")

def musique():
    print("hello")

def charger_image(url):
    image = ctk.CTkImage(light_image=Image.open(url), size= (50,50))
    return image

def placer_app(frame,icone,lancerapp,ligne,colonne):
    frame.columnconfigure((0,1,2,3), weight=1)
    frame.rowconfigure((0,1,2,3), weight=1)

    #Applications
    buttonapp = ctk.CTkButton(master=frame,image=icone,text="",command=lancerapp,width=50,height=50,fg_color="transparent",border_width=0,corner_radius=0,hover=False)
    buttonapp.grid(row=ligne,column=colonne,padx=10,pady=10,sticky="w")


app = ctk.CTk()
app.title("Prototype")
app.geometry("400x700")
app.iconbitmap("img/logo.ico")
app.resizable(width=False,height=False)
app.grid_rowconfigure(0, weight=1)  # écran principal
app.grid_rowconfigure(1, weight=0)  # barre du bas
app.grid_columnconfigure(0, weight=1)
frame_music = Frame(app, bg="#686868")
frame_music.grid(row=0, column=0, sticky="nsew")
frame_barre = Frame(app, height=90, bg="#c1c1c1")
frame_barre.grid(row=1, column=0, sticky="ew")
frame_barre.grid_propagate(False)

icone_play = charger_image("img/play.png")
icone_pause = charger_image("img/pause.png")
icone_sup = charger_image("img/superieur.png")
icone_inf = charger_image("img/inferieur.png")

placer_app(frame_music,icone_play,play,0,0)
placer_app(frame_music,icone_pause,pause,0,1)
placer_app(frame_music,icone_sup,suivant,0,2)
placer_app(frame_music,icone_inf,retour,0,3)

app.mainloop()