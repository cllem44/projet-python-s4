import customtkinter as ctk
from img import *
import PIL.Image as PilImage
from Frame_ecranprincipal import *
from application.Music import *
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from application.meteo import creer_meteo
from application.horloge import creer_horloge
from application.Music import creer_music
from application.bloc_notes.Bloc_notes import creer_bloc_notes
from application.GPS import creer_map
from application.Morpion import creer_morpion
from application.Parametre import creer_parametre
from application.Parametre import init_frames
from application.Parametre import init_economiseur
from application.Parametre import init_volume
from application.Parametre import init_luminosite
from application.Parametre import init_barrebas
from application.Parametre import init_ecran_accueil
import screen_brightness_control as sbc

debut_x = 0
debut_y = 0
timer_id = None
Delai_inactivite = 30000

def set_delai(ms):
    global Delai_inactivite
    Delai_inactivite = ms
    reinitialiser_timer()  

def set_luminosite(valeur):
    sbc.set_brightness(int(float(valeur)))

def reinitialiser_timer(event=None):
    global timer_id
    if timer_id:
        app.after_cancel(timer_id)  
    timer_id = app.after(Delai_inactivite, eteindretelephone)  


def afficher_ecran(ancien_frame,nouveau_frame):
    global frame_actif
    ancien_frame.grid_remove()
    nouveau_frame.grid(row=0, column=0, sticky="nsew")
    frame_actif = nouveau_frame

def eteindretelephone():
    afficher_ecran(frame_actif,frame_verrouille)

def set_ecran_accueil(num):
    global ecran_accueil_ref
    if num == 1:
        ecran_accueil_ref = frame_ecran1
    elif num == 2:
        ecran_accueil_ref = frame_ecran2

def ecranaccueil():
    afficher_ecran(frame_actif,ecran_accueil_ref)

def debutswipe(event):
    global debut_x, debut_y
    debut_x = event.x
    debut_y = event.y

def finswipe(event):
    dx = event.x - debut_x
    dy = event.y - debut_y
    if abs(dx) > abs(dy):
        if dx < 20:
            afficher_ecran(frame_ecran1,frame_ecran2)
        elif dx > -20:
            afficher_ecran(frame_ecran2,frame_ecran1)


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

# Délai
init_economiseur(set_delai)
app.bind_all("<Any-KeyPress>", reinitialiser_timer)
app.bind_all("<Any-Button>", reinitialiser_timer)
app.bind_all("<Motion>", reinitialiser_timer)
reinitialiser_timer()

# Volume depuis parametre
init_volume(diminuerson, augmenterson)

# FRAMES 
frame_ecran1, frame_ecran2, frame_verrouille, frame_barre = creer_frames(app)
setup_frames(frame_barre,eteindretelephone,diminuerson,augmenterson,ecranaccueil)
afficher_ecran(frame_ecran2,frame_ecran1)

# Fond d'écrans
label = setup_fond(frame_ecran1,"img/fondecran/ecran1.png")
label2 = setup_fond(frame_ecran2,"img/fondecran/ecran2.png")
init_frames(label,label2)
init_luminosite(set_luminosite)
init_barrebas(frame_barre)
label.bind("<ButtonPress-1>", debutswipe)
label.bind("<ButtonRelease-1>", finswipe)
label2.bind("<ButtonPress-1>", debutswipe)
label2.bind("<ButtonRelease-1>", finswipe)

ecran_accueil_ref = frame_ecran1
init_ecran_accueil(set_ecran_accueil)
#Applications

frame_meteo = creer_meteo(app)
frame_meteo.grid_remove()


app_meteo = charger_image("img/app_meteo.png")
placer_app(frame_ecran1, app_meteo, lambda: afficher_ecran(frame_actif, frame_meteo), 0, 0)

frame_horloge = creer_horloge(app)
frame_horloge.grid_remove()

app_horloge = charger_image("img/app_horloge.png")
placer_app(frame_ecran1, app_horloge, lambda: afficher_ecran(frame_actif, frame_horloge), 1, 0)

frame_music = creer_music(app)
frame_music.grid_remove()

app_musique = charger_image("img/app_musique.png")
placer_app(frame_ecran1, app_musique, lambda: afficher_ecran(frame_actif, frame_music), 2, 0)

frame_bloc_notes = creer_bloc_notes(app)
frame_bloc_notes.grid_remove()

app_bloc_notes = charger_image("img/app_bloc_note.png")
placer_app(frame_ecran1, app_bloc_notes, lambda: afficher_ecran(frame_actif, frame_bloc_notes), 2, 1)

'''frame_bataille_navale= creer_bataille_navale(app)
frame_bataille_navale.grid_remove()

app_bataille_navale = charger_image("img/app_bataille_navale.png")
placer_app(frame_ecran1, app_bataille_navale, lambda: afficher_ecran(frame_actif, frame_bataille_navale), 2, 1)
'''
frame_GPS = creer_map(app)
frame_GPS.grid_remove()

app_GPS = charger_image("img/app_map.png")
placer_app(frame_ecran1,app_GPS, lambda: afficher_ecran(frame_actif, frame_GPS), 0, 1)

frame_parametre = creer_parametre(app)
frame_parametre.grid_remove()

app_parametre = charger_image("img/app_parametre.png")
placer_app(frame_ecran1,app_parametre, lambda: afficher_ecran(frame_actif, frame_parametre), 1, 1)

frame_morpion = creer_morpion(app)
frame_morpion.grid_remove()

app_morpion = charger_image("img/app_morpion.png")
placer_app(frame_ecran2,app_morpion, lambda: afficher_ecran(frame_actif, frame_morpion), 0, 0)

app.mainloop()