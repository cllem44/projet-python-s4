import customtkinter as ctk
from tkinter import *
from tkinter import filedialog
from PIL import Image
import os 
import pyglet

def creer_music (app):
    musiques = []
    musique_actuelle = ""
    Pause = False
    player = pyglet.media.Player()

    def charger_musique():
        global musique_actuelle,musiques

        musiques.clear()
        listeChanson.delete(0,END)
        app.directory = filedialog.askdirectory()
        
        for musique in os.listdir(app.directory):
            nom,ext =os.path.splitext(musique)
            if ext == ".mp3":
                musiques.append(musique)
        
        for musique in musiques:
            listeChanson.insert("end",musique)

        listeChanson.selection_set(0)
        musique_actuelle = musiques[listeChanson.curselection()[0]]

    def play():
        global musique_actuelle, Pause , player
        if Pause:
            player.play()
            Pause = False
            return
        player.pause()
        player = pyglet.media.Player()
        source = pyglet.media.load(os.path.join(app.directory, musique_actuelle))
        player.queue(source)
        player.play()


    def pause():
        global Pause
        player.pause()
        Pause = True

    def precedent():
        global musique_actuelle
        index = musiques.index(musique_actuelle)
        if index > 0:
            index -= 1
        listeChanson.selection_clear(0, END)
        listeChanson.selection_set(index)
        musique_actuelle = musiques[index]
        play()

    def suivant():
        global musique_actuelle
        index = musiques.index(musique_actuelle)
        if index < len(musiques) - 1:
            index += 1
        listeChanson.selection_clear(0, END)
        listeChanson.selection_set(index)
        musique_actuelle = musiques[index]
        play()

    def musique():
        print("hello")

    def charger_image(url):
        image = ctk.CTkImage(light_image=Image.open(url), size= (50,50))
        return image



    frame_music_general = Frame(app, background="#000000")
    frame_music_general.grid(row=0, column=0, sticky="nsew")
    frame_music_general.grid_remove()

    frame_music_general.grid_rowconfigure(0, weight=1)
    frame_music_general.grid_rowconfigure(1, weight=0)
    frame_music_general.grid_columnconfigure(0, weight=1)

    frame_music = Frame(frame_music_general, bg="#FFFEFE")
    frame_music.grid(row=0, column=0, sticky="nsew")
    frame_btnmusique = Frame(frame_music_general, bg ="#FFFFFF")
    frame_btnmusique.grid(row=1, column=0, sticky ="ew")
    frame_btnmusique.grid_columnconfigure((0,1,2,3), weight=1)
    frame_barre = Frame(frame_music_general, height=90, bg="#c1c1c1")
    frame_barre.grid(row=2, column=0, sticky="ew")
    frame_barre.grid_propagate(False)

    menubar = Menu(frame_music_general)
    app.config(menu=menubar)
    organise_menu = Menu(menubar,tearoff=False)
    organise_menu.add_command(label="Choississez votre dossier avec les musiques",command=charger_musique)
    menubar.add_cascade(label="Playlist",menu =organise_menu)

    listeChanson = Listbox(frame_music,bg ='black',fg = "white",width=100, height = 100)
    listeChanson.grid(row=0,column=0, sticky="ns")

    icone_play = charger_image("img/musique/play.png")
    icone_pause = charger_image("img/musique/pause.png")
    icone_sup = charger_image("img/musique/superieur.png")
    icone_inf = charger_image("img/musique/inferieur.png")

    buttonplay = ctk.CTkButton(master=frame_btnmusique,image=icone_play,text="",command=play,width=50,height=50,fg_color="transparent",border_width=0,corner_radius=0,hover=False)
    buttonplay.grid(row=2,column=1,padx=0,pady=0,sticky="w")
    buttonpause = ctk.CTkButton(master=frame_btnmusique,image=icone_pause,text="",command=pause,width=50,height=50,fg_color="transparent",border_width=0,corner_radius=0,hover=False)
    buttonpause.grid(row=2,column=2,padx=0,pady=0,sticky="w")
    buttonprecedent = ctk.CTkButton(master=frame_btnmusique,image=icone_inf,text="",command=precedent,width=50,height=50,fg_color="transparent",border_width=0,corner_radius=0,hover=False)
    buttonprecedent.grid(row=2,column=0,padx=0,pady=0,sticky="w")
    buttonsuivant = ctk.CTkButton(master=frame_btnmusique,image=icone_sup,text="",command=suivant,width=50,height=50,fg_color="transparent",border_width=0,corner_radius=0,hover=False)
    buttonsuivant.grid(row=2,column=3,padx=0,pady=0,sticky="w")

    return frame_music_general


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Prototype")
    app.iconbitmap("img/logo.ico")
    app.geometry("400x700")
    app.resizable(width=False, height=False)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    creer_music(app)