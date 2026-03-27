import customtkinter as ctk
from tkinter import *
from PIL import Image
import PIL.Image as PilImage
import os
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
def creer_parametre(app):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    label_ecran1 = None
    label_ecran2 = None

    def init_frames(l_ecran1, l_ecran2):
        global label_ecran1, label_ecran2
        label_ecran1 = l_ecran1
        label_ecran2 = l_ecran2


    def setup_fond(frame, chemin):
        image_pil = PilImage.open(chemin)
        image_ctk = ctk.CTkImage(image_pil, size=(400, 640))
        label = ctk.CTkLabel(frame, image=image_ctk, text="")
        label.place(relwidth=1, relheight=1)
        return label

    ecran_selectionne = None
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

        if ecran_selectionne is None:
            return

        chemin_complet = os.path.normpath(os.path.join(BASE_DIR, "..", chemin))

        image_pil = PilImage.open(chemin_complet)
        image_ctk = ctk.CTkImage(light_image=image_pil, size=(400, 640))

        if ecran_selectionne == 1 and label_ecran1:
            label_ecran1.configure(image=image_ctk)
            label_ecran1._image_ref = image_ctk 
        elif ecran_selectionne == 2 and label_ecran2:
            label_ecran2.configure(image=image_ctk)
            label_ecran2._image_ref = image_ctk

    def changer_page(option):
        for widget in frame_contenu.winfo_children():
            widget.destroy()
        
        if option == "Fond d'ecrans":
            changer_fondecran()

        elif option == "Applications":
            changer_application()

    def placer_fond():
        ecran1 = charger_image("img/fondecran/ecran1.png")
        placer_app(frame_contenu,ecran1,"img/fondecran/ecran1.png",2,0)

        ecran2 = charger_image("img/fondecran/ecran2.png")
        placer_app(frame_contenu,ecran2,"img/fondecran/ecran2.png",2,1)

        ecran3 = charger_image("img/fondecran/ecran3.png")
        placer_app(frame_contenu,ecran3,"img/fondecran/ecran3.png",3,0)

        ecran4 = charger_image("img/fondecran/ecran4.png")
        placer_app(frame_contenu,ecran4,"img/fondecran/ecran4.png",3,1)

        ecran5 = charger_image("img/fondecran/ecran5.png")
        placer_app(frame_contenu,ecran5,"img/fondecran/ecran5.png",4,0)

        ecran6 = charger_image("img/fondecran/ecran6.png")
        placer_app(frame_contenu,ecran6,"img/fondecran/ecran6.png",4,1)


    def changer_fondecran():
        global btn_ecran1,btn_ecran2
        Label(frame_contenu, text="Fond d'écrans", bg="#2b2b2b", fg="white",font=("Arial", 15)).grid(row=0, column=0, pady=20, padx =50)
        btn_ecran1 = ctk.CTkButton(master=frame_contenu,text="Ecran 1",height=40,width= 80,anchor="w",fg_color="transparent",text_color="white",border_width=0,corner_radius=10,hover=True,command=lambda:recuperer_ecran(1))
        btn_ecran1.grid(row=1,column=0,pady=2,padx=5)
        btn_ecran2 = ctk.CTkButton(master=frame_contenu,text="Ecran 2",height=40,width= 80,anchor="w",fg_color="transparent",text_color="white",border_width=0,corner_radius=10,hover=True,command=lambda:recuperer_ecran(2))
        btn_ecran2.grid(row=1,column=1,pady=2,padx=5)
        placer_fond()

    def changer_application():
        Label(frame_contenu, text="Applications", bg="#2b2b2b", fg="white",font=("Arial", 15)).grid(row=0, column=0, pady=20, padx=50)

    def recuperer_ecran(num):
        global ecran_selectionne
        if num == 1:
            ecran_selectionne = 1
            btn_ecran1.configure(fg_color="#555555")
            btn_ecran2.configure(fg_color="transparent")
        elif num == 2:
            ecran_selectionne = 2
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

    # --------Scrollbar---------------
    frame_option = ctk.CTkScrollableFrame(frame_haut, width=120, fg_color="#898989", scrollbar_button_color="#898989", scrollbar_button_hover_color="#707070")
    frame_option.grid(row=0, column=0, sticky="nsew")


    # ----------Boutons Options ------------
    options = ["Fond d'ecrans","Applications"]
    frame_option.grid_columnconfigure(0,weight=1)
    for i,option in enumerate(options):
        btn = ctk.CTkButton(master=frame_option,text=option,height=40,anchor="w",fg_color="transparent",text_color="white",border_width=0,corner_radius=10,hover=True,command=lambda o=option: changer_page(o))
        btn.grid(row=i,column=0,pady=2,padx=5,sticky="ew")


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

    return frame_parametre_general