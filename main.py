import customtkinter as ctk
from img import *
import PIL.Image as PilImage
from Frame_ecranprincipal import *
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

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

app.mainloop()
