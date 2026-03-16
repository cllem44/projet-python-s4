import customtkinter as ctk
from img import *
import PIL.Image as PilImage
from Frame_ecranprincipal import *
from application.Music import *
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

debut_x = 0
debut_y = 0

def afficher_ecran(frame):
    for f in (frame_ecran1, frame_ecran2, frame_verrouille):
        f.grid_remove()
    frame.grid(row=0, column=0, sticky="nsew")

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


devices = AudioUtilities.GetSpeakers()
interface = devices._dev.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

def diminuerson():
    current = volume.GetMasterVolumeLevelScalar()  
    new = max(0.0, current - 0.05)  
    volume.SetMasterVolumeLevelScalar(new, None)

def augmenterson():
    current = volume.GetMasterVolumeLevelScalar()
    new = min(1.0, current + 0.05) 
    volume.SetMasterVolumeLevelScalar(new, None)

def setup_fond(frame, chemin):
    image_pil = PilImage.open(chemin)
    image_ctk = ctk.CTkImage(image_pil, size=(400, 640))
    label = ctk.CTkLabel(frame, image=image_ctk, text="")
    label.place(relwidth=1, relheight=1)
    return label

# customtkinter
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
setup_frames(frame_barre,eteindretelephone,diminuerson,augmenterson,ecranaccueil)
afficher_ecran(frame_ecran1)

# Fond d'écrans
label = setup_fond(frame_ecran1,"img/ecran1.png")
label2 = setup_fond(frame_ecran2,"img/ecran2.png")
label.bind("<ButtonPress-1>", debutswipe)
label.bind("<ButtonRelease-1>", finswipe)
label2.bind("<ButtonPress-1>", debutswipe)
label2.bind("<ButtonRelease-1>", finswipe)

#Applications
app1 = charger_image("img/appmusique.png")
placer_app(frame_ecran1,app1,musique,0,0,debutswipe,finswipe) # marche mieux avec label au lieu de frame_ecran1 mais ca me parait bizarre, demander a la prof 

app.mainloop()
#tkinter



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
