import customtkinter as ctk
from tkinter import *
from PIL import Image
import PIL.Image as PilImage
import os
import screen_brightness_control as sbc

# ------- Variables utiles pour gérer des changements dans le fichier main (c'est les fonctions qui sont utiles dans les faits mais elles restent utiles tout de même) ------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
label_ecran1 = None
label_ecran2 = None
changer_delai = None
diminuer_vol = None
augmenter_vol = None
luminosite = None
barre_bas = None
ecran_accueil = None

def init_frames(l_ecran1, l_ecran2):
    global label_ecran1, label_ecran2
    label_ecran1 = l_ecran1
    label_ecran2 = l_ecran2
    #print(label_ecran1,label_ecran2)

def init_economiseur(nouveau):
    global changer_delai
    changer_delai = nouveau

def changer_delai(ms):
    if changer_delai:
        changer_delai(ms)

def init_volume(diminuer, augmenter):
    global diminuer_vol, augmenter_vol
    diminuer_vol = diminuer
    augmenter_vol = augmenter

def init_luminosite(lum):
    global luminosite
    luminosite = lum

def init_barrebas(frame_barre):
    global barre_bas
    barre_bas = frame_barre

COULEURS = {
    "Gris":     "#c1c1c1",
    "Noir":     "#1a1a1a",
    "Blanc":    "#ffffff",
    "Bleu":     "#1a73e8",
    "Rouge":    "#e53935",
    "Vert":     "#43a047",
    "Violet":   "#8e24aa",
    "Orange":   "#fb8c00",
}

def init_ecran_accueil(ecran):
    global ecran_accueil
    ecran_accueil = ecran

# -------- FONCTION PRINCIPALE ---------
def creer_parametre(app):
    etat= {"ecran_selectionne": None}
    def charger_image(url):
        image = ctk.CTkImage(light_image=Image.open(url), size= (50,50))
        return image

    def placer_app(frame,icone,chemin,ligne,colonne):
        frame.columnconfigure((0,1,2), weight=0)
        frame.rowconfigure((0,1,2,3,4), weight=0)

        #Applications
        buttonapp = ctk.CTkButton(master=frame,image=icone,text="",command=lambda:misajour_fondecran(chemin),width=50,height=50,fg_color="transparent",bg_color="transparent",border_width=0,corner_radius=0,hover=False)
        buttonapp.grid(row=ligne,column=colonne,padx=10,pady=10,sticky="w")

    def misajour_fondecran(chemin):
        global label_ecran1, label_ecran2
        #print("ecran =", etat["ecran_selectionne"])
        #print("label1 =", label_ecran1)
        #print("label2 =", label_ecran2)

        if etat["ecran_selectionne"] is None:
            msg_erreur.grid(row=5, column=0, pady=5, padx=10)
            return
        msg_erreur.grid_remove()
        chemin_complet = os.path.normpath(os.path.join(BASE_DIR, "..", chemin))
        #print("chemin_complet =", chemin_complet)  

        image_pil = PilImage.open(chemin_complet)
        image_ctk = ctk.CTkImage(light_image=image_pil, size=(400, 640))

        if etat["ecran_selectionne"] == 1:
            label_ecran1.configure(image=image_ctk)
        elif etat["ecran_selectionne"] == 2:
            label_ecran2.configure(image=image_ctk)
        


    def changer_page(option):
        for widget in frame_contenu.winfo_children():
            widget.destroy()
        
        if option == "Fond d'ecrans":
            changer_fondecran()

        elif option == "Economiseur":
            changer_economiseur()

        elif option == "Volume":
            changer_volume()
        
        elif option == "Luminosite":
            changer_luminosite()
        
        elif option == "Couleur Barre":
            changer_barre()

        elif option == "Écran d'accueil":
            changer_ecran_accueil()

    def placer_fond():
        fonds = [
                ("img/fondecran/ecran1.png", 2, 0),
                ("img/fondecran/ecran2.png", 2, 1),
                ("img/fondecran/ecran3.png", 3, 0),
                ("img/fondecran/ecran4.png", 3, 1),
                ("img/fondecran/ecran5.png", 4, 0),
                ("img/fondecran/ecran6.png", 4, 1),
                ]
        for chemin, ligne, colonne in fonds:
            chemin_complet = os.path.normpath(os.path.join(BASE_DIR, "..", chemin))
            icone = charger_image(chemin_complet)
            placer_app(frame_contenu, icone, chemin, ligne, colonne)


    def changer_fondecran():
        global btn_ecran1,btn_ecran2,msg_erreur
        Label(frame_contenu, text="Fond d'écrans", bg="#2b2b2b", fg="white",font=("Arial", 15)).grid(row=0, column=0, pady=20, padx =50)
        btn_ecran1 = ctk.CTkButton(master=frame_contenu,text="Ecran 1",height=40,width= 80,anchor="w",fg_color="transparent",text_color="white",border_width=0,corner_radius=10,hover=True,command=lambda:recuperer_ecran(1))
        btn_ecran1.grid(row=1,column=0,pady=2,padx=5)
        btn_ecran2 = ctk.CTkButton(master=frame_contenu,text="Ecran 2",height=40,width= 80,anchor="w",fg_color="transparent",text_color="white",border_width=0,corner_radius=10,hover=True,command=lambda:recuperer_ecran(2))
        btn_ecran2.grid(row=1,column=1,pady=2,padx=5)
        msg_erreur = Label(frame_contenu, text="Aucun écran sélectionné", bg="#2b2b2b", fg="white",font=("Arial", 15))
        msg_erreur.grid_remove()
        placer_fond()

    def changer_economiseur():
        Label(frame_contenu, text="Economiseur d'écran", bg="#2b2b2b", fg="white",font=("Arial", 15)).grid(row=0, column=0, pady=20, padx=50)
        Label(frame_contenu, text="Délai d'inactivité", bg="#2b2b2b", fg="white",font=("Arial", 13)).grid(row=1, column=0, pady=20, padx=50)
        label_valeur = Label(frame_contenu, text="30 sec", bg="#2b2b2b", fg="white",font=("Arial", 13))
        label_valeur.grid(row=2, column=0)

        def maj_delai(valeur):
            secondes = int(float(valeur))
            label_valeur.config(text=f"{secondes} sec")
            changer_delai(secondes * 1000)  

        slider = ctk.CTkSlider(frame_contenu, from_=10, to=120,command=maj_delai, width=200)
        slider.set(30)  
        slider.grid(row=3, column=0, pady=10, padx=10)
    
    def changer_volume():
        Label(frame_contenu, text="Volume", bg="#2b2b2b", fg="white",font=("Arial", 15)).grid(row=0, column=0, pady=20, padx=50)       
        btn_moins = ctk.CTkButton(frame_contenu, text="-", width=60, height=60,font=("Arial", 30), command=diminuer_vol)
        btn_moins.grid(row=1, column=0, padx=10, pady=20)

        btn_plus = ctk.CTkButton(frame_contenu, text="+", width=60, height=60,font=("Arial", 30), command=augmenter_vol)
        btn_plus.grid(row=1, column=1, padx=10, pady=20)
    
    def changer_luminosite():
        Label(frame_contenu, text="Luminosite", bg="#2b2b2b", fg="white",font=("Arial", 15)).grid(row=0, column=0, pady=20, padx=50)      
        label_valeur = Label(frame_contenu, bg="#2b2b2b", fg="white",font=("Arial", 13))
        label_valeur.grid(row=1, column=0)
        def maj_luminosite(valeur):
            txt = int(float(valeur))
            label_valeur.config(text=f"{txt}%")
            if luminosite:
                luminosite(valeur)
        luminosite_actuelle = sbc.get_brightness()[0]
        slider = ctk.CTkSlider(frame_contenu,from_=0,to=100,command=maj_luminosite,width=200)
        slider.set(luminosite_actuelle)
        label_valeur.config(text=f"{luminosite_actuelle}%")
        slider.grid(row=2,column=0,padx=10,pady=10)
    
    def changer_barre():
        Label(frame_contenu, text="Couleur Barre", bg="#2b2b2b", fg="white",font=("Arial", 15)).grid(row=0, column=0, pady=20, padx=50)      
        for i,(nom,hex) in enumerate(COULEURS.items()):
            btn = ctk.CTkButton(master=frame_contenu,text=nom,width=100, height=35,fg_color=hex,text_color="white" if hex != "#ffffff" else "black",corner_radius=8,command=lambda h=hex: appliquer_couleur_barre(h))
            btn.grid(row=1 + i // 2, column=i % 2, padx=8, pady=5)
    def appliquer_couleur_barre(hex):
        if barre_bas:
            barre_bas.configure(bg=hex)
            for widget in barre_bas.winfo_children():
                try:
                    widget.configure(fg_color=hex)
                except:
                    widget.configure(bg=hex)
    
    def changer_ecran_accueil():
        Label(frame_contenu, text="Ecran d'accueil", bg="#2b2b2b", fg="white",font=("Arial", 15)).grid(row=0, column=0, pady=20, padx=50)      
        def appliquer_ecran_acceuil(num):
            if ecran_accueil:
                ecran_accueil(num)
            btn1.configure(fg_color="#555555" if num == 1 else "transparent")
            btn2.configure(fg_color="#555555" if num == 2 else "transparent")           
        btn1 = ctk.CTkButton(frame_contenu, text="Écran 1", width=100, height=40,fg_color="transparent", text_color="white",corner_radius=10, command=lambda: appliquer_ecran_acceuil(1))
        btn1.grid(row=1, column=0, padx=8, pady=10)

        btn2 = ctk.CTkButton(frame_contenu, text="Écran 2", width=100, height=40,fg_color="transparent", text_color="white",corner_radius=10, command=lambda: appliquer_ecran_acceuil(2))
        btn2.grid(row=1, column=1, padx=8, pady=10)
        
    def recuperer_ecran(num):
        
        if num == 1:
            etat["ecran_selectionne"] = 1
            btn_ecran1.configure(fg_color="#555555")
            btn_ecran2.configure(fg_color="transparent")
        elif num == 2:
            etat["ecran_selectionne"] = 2
            btn_ecran2.configure(fg_color="#555555")
            btn_ecran1.configure(fg_color="transparent")
            return 2
        else:
            return

    # ------------FRAMES -------------
    frame_parametre_general = Frame(app, background="#000000")
    frame_parametre_general.grid(row=0, column=0, sticky="nsew")
    frame_parametre_general.grid_columnconfigure(0, weight=1)
    frame_parametre_general.grid_rowconfigure(0,weight=1)
    frame_parametre_general.grid_rowconfigure(1,weight=0)

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

    

    # --------SCROLLBAR---------------
    frame_option = ctk.CTkScrollableFrame(frame_haut, width=120, fg_color="#898989", scrollbar_button_color="#898989", scrollbar_button_hover_color="#707070")
    frame_option.grid(row=0, column=0, sticky="nsew")


    # ----------BUTTONS OPTIONS ------------
    options = ["Fond d'ecrans","Economiseur","Volume","Luminosite","Couleur Barre","Écran d'accueil"]
    frame_option.grid_columnconfigure(0,weight=1)
    for i,option in enumerate(options):
        btn = ctk.CTkButton(master=frame_option,text=option,height=40,anchor="w",fg_color="transparent",text_color="white",border_width=0,corner_radius=10,hover=True,command=lambda o=option: changer_page(o))
        btn.grid(row=i,column=0,pady=2,padx=5,sticky="ew")


    
    return frame_parametre_general

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Prototype")
    app.iconbitmap("img/logo.ico")
    app.geometry("400x700")
    app.resizable(width=False, height=False)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    
    # Appel pour tester l'écran individuellement
    frame_parametre = creer_parametre(app)
    frame_parametre.grid(row=0, column=0, sticky="nsew")
    
    app.mainloop()