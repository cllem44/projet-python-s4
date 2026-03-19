from meteofrance_api import MeteoFranceClient
import customtkinter as ctk
from tkinter import Frame, Label, Entry, Button  
from PIL import Image, ImageTk                   
from datetime import datetime






# ── API ───────────────────────────────────────────────────────────────────────

def API_meteo(nom_ville):
    client = MeteoFranceClient()
    places = client.search_places(nom_ville)

    if not places:
        return "Ville introuvable", None ,None

    my_place = places[0]
    forecast = client.get_forecast_for_place(my_place)
    current_forecast = forecast.current_forecast

    if current_forecast:
        temp = current_forecast['T']['value']
        desc = current_forecast['weather']['icon']
         
        jour_future = []
                
        for day in forecast.daily_forecast[1:6]:
        
            date = datetime.fromtimestamp(day['dt']).strftime('%d/%m')
            
            
            t_min = day.get('T', {}).get('min', 'N/A')
            t_max = day.get('T', {}).get('max', 'N/A')
            
            weather_12h = day.get('weather12H', {})
            icon = weather_12h.get('icon', 'Description non disponible')
            jour_future.append([date,t_min,t_max,icon])
        #print(jour_future)
        return f"{temp}°C", desc, jour_future
        

    return "Données indisponibles", None , None
    


# ── Icône ─────────────────────────────────────────────────────────────────────
def get_icon_image(code, taille=100):
    #print("code :", code)

    if not code:
        icon_name = "erreur-404"
    else:
        code_sans_p = code[1:]
        jour_ou_nuit = code_sans_p[-1]
        milieu = code_sans_p[:-1]
        milieu_original = milieu  # sauvegarde avant modification

        if milieu.endswith("bis"):
            milieu = milieu[:-3]
        elif milieu.endswith("ter"):
            milieu = milieu[:-3]

        numero = int(milieu)

        if numero == 1 and jour_ou_nuit == "j":
            icon_name = "soleil"
        elif jour_ou_nuit == "n" and numero <= 4:
            icon_name = "pleine-lune"
        elif numero <= 4:
            icon_name = "nuageux"
        elif numero in range(16, 33):
            icon_name = "orage"
        elif numero in range(5, 8):
            icon_name = "pluvieux"
        elif numero in range(8, 12):
            icon_name = "neige"
        elif numero == 13 and milieu_original.endswith("ter"):
            icon_name = "neige"
        else:
            icon_name = "pluie"

    chemin = f"img/meteo/{icon_name}.png"
    image = Image.open(chemin).resize((taille, taille))
    return ImageTk.PhotoImage(image)
# ── Actions ───────────────────────────────────────────────────────────────────

def afficher_valeur():
    valeur_saisie = ville_champ.get()

    affiche_ville.config(text=valeur_saisie.capitalize())
    label_temp_J.config(text="Recherche en cours...")
    #app.update()

    meteo_actuelle, icon ,liste_jours_desc= API_meteo(valeur_saisie)
    label_temp_J.config(text=meteo_actuelle)
    # ── Jour J ───────────────────────────────────────────────────────────────────
    try:
        img_object = get_icon_image(icon, taille=200)
        #print('jour J   icon ;',icon,"     img_object :",img_object)
        label_icon_jour.config(image=img_object)
        label_icon_jour.image = img_object
   
    except Exception as e:
        print(f"Erreur de chargement de l'image : {e}")
        label_icon_jour.config(image="")
        label_icon_jour.image = None
    # ── Jour + 1 ───────────────────────────────────────────────────────────────────
    try:
        img_object = get_icon_image(liste_jours_desc[0][3], taille=150)
        #print('jour J1   icon ;',icon,"     img_object :",img_object)
        label_icon_jour_p1.config(image=img_object)
        label_icon_jour_p1.image = img_object
        label_temp_J1.config(text=f"{liste_jours_desc[0][1]}/{liste_jours_desc[0][2]}°C\n{liste_jours_desc[0][0]}")
   
    except Exception as e:
        print(f"Erreur de chargement de l'image : {e}")
        label_icon_jour_p1.config(image="")
        label_icon_jour_p1.image = None
    # ── Jour + 2 ───────────────────────────────────────────────────────────────────
    try:
        img_object = get_icon_image(liste_jours_desc[1][3], taille=150)
        #print('jour J2   icon ;',icon,"     img_object :",img_object)
        label_icon_jour_p2.config(image=img_object)
        label_icon_jour_p2.image = img_object 
        label_temp_J2.config(text=f"{liste_jours_desc[1][1]}/{liste_jours_desc[1][2]}°C\n{liste_jours_desc[1][0]}")
   
    except Exception as e:
        print(f"Erreur de chargement de l'image : {e}")
        label_icon_jour_p2.config(image="")
        label_icon_jour_p2.image = None

    # ── Jour + 3 ───────────────────────────────────────────────────────────────────
    try:
        img_object = get_icon_image(liste_jours_desc[2][3], taille=150)
        #print('jour J3   icon ;',icon,"     img_object :",img_object)
        label_icon_jour_p3.config(image=img_object)
        label_icon_jour_p3.image = img_object  
        label_temp_J3.config(text=f"{liste_jours_desc[2][1]}/{liste_jours_desc[2][2]}°C\n{liste_jours_desc[2][0]}")
   
    except Exception as e:
        print(f"Erreur de chargement de l'image : {e}")
        label_icon_jour_p3.config(image="")
        label_icon_jour_p3.image = None

    # ── Jour + 4 ───────────────────────────────────────────────────────────────────
    try:
        img_object = get_icon_image(liste_jours_desc[3][3], taille=150)
        #print('jour J4   icon ;',icon,"     img_object :",img_object)
        label_icon_jour_p4.config(image=img_object)
        label_icon_jour_p4.image = img_object  
        label_temp_J4.config(text=f"{liste_jours_desc[3][1]}/{liste_jours_desc[3][2]}°C\n{liste_jours_desc[3][0]}")
   
    except Exception as e:
        print(f"Erreur de chargement de l'image : {e}")
        label_icon_jour_p4.config(image="")
        label_icon_jour_p4.image = None

    # ── Jour + 5 ───────────────────────────────────────────────────────────────────    
    try:
        img_object = get_icon_image(liste_jours_desc[4][3], taille=150)
        #print('jour J5   icon ;',icon,"     img_object :",img_object)
        label_icon_jour_p5.config(image=img_object)
        label_icon_jour_p5.image = img_object  
        label_temp_J5.config(text=f"{liste_jours_desc[4][1]}/{liste_jours_desc[4][2]}°C\n{liste_jours_desc[4][0]}")
   
    except Exception as e:
        print(f"Erreur de chargement de l'image : {e}")
        label_icon_jour_p5.config(image="")
        label_icon_jour_p5.image = None


# ── Interface ─────────────────────────────────────────────────────────────────

""""""
def creer_meteo (app):
    global ville_champ,affiche_ville,label_temp_J,label_temp_J1,label_temp_J2,label_temp_J3,label_temp_J4,label_temp_J5,label_icon_jour,label_icon_jour_p1,label_icon_jour_p2,label_icon_jour_p3,label_icon_jour_p4,label_icon_jour_p5
    

    frame_meteo = Frame(app, background="#2eafff")
    frame_meteo.grid(row=0, column=0, sticky="nsew")
    frame_meteo.grid_columnconfigure(0, weight=1)

    affiche_ville = Label( master=frame_meteo, text="Entrez une ville",fg="#FFFFFF", bg="#2eafff",font=("Arial", 40, "bold"))
    affiche_ville.grid(column=0, row=0, sticky="n", pady=(30, 20),columnspan=5)

    ville_champ = Entry(master=frame_meteo, bg="white", font=("Arial", 30), justify="center")
    ville_champ.grid(column=0, row=1, sticky="n", pady=40, columnspan=5)

    bouton_valider = Button(master=frame_meteo, text="Rechercher", font=("Arial", 30), command=afficher_valeur)
    bouton_valider.grid(column=0, row=2, sticky="n", pady=10, columnspan=5)

    label_icon_jour = Label(master=frame_meteo, image="", bg="#2eafff")
    label_icon_jour.grid(column=0, row=3, sticky="n", pady=40, columnspan=5)

    label_temp_J = Label(master=frame_meteo, text="", fg="#FFFFFF", bg="#2eafff", font=("Arial", 35))
    label_temp_J.grid(column=0, row=4, sticky="n", pady=40, columnspan=5)

    label_icon_jour_p1 = Label(master=frame_meteo, image="", bg="#2eafff")
    label_icon_jour_p1.grid(column=0, row=5, sticky="n", pady=40,padx=5)

    label_icon_jour_p2 = Label(master=frame_meteo, image="", bg="#2eafff")
    label_icon_jour_p2.grid(column=1, row=5, sticky="n", pady=40,padx=5)

    label_icon_jour_p3 = Label(master=frame_meteo, image="", bg="#2eafff")
    label_icon_jour_p3.grid(column=2, row=5, sticky="n", pady=40,padx=5)

    label_icon_jour_p4 = Label(master=frame_meteo, image="", bg="#2eafff")
    label_icon_jour_p4.grid(column=3, row=5, sticky="n", pady=40,padx=5)

    label_icon_jour_p5 = Label(master=frame_meteo, image="", bg="#2eafff")
    label_icon_jour_p5.grid(column=4, row=5, sticky="n", pady=40,padx=5)

    label_temp_J1 = Label(master=frame_meteo, text="", fg="#FFFFFF", bg="#2eafff", font=("Arial", 20))
    label_temp_J1.grid(column=0, row=6, sticky="n", pady=20,padx=5)

    label_temp_J2 = Label(master=frame_meteo, text="", fg="#FFFFFF", bg="#2eafff", font=("Arial", 20))
    label_temp_J2.grid(column=1, row=6, sticky="n", pady=20,padx=5)

    label_temp_J3 = Label(master=frame_meteo, text="", fg="#FFFFFF", bg="#2eafff", font=("Arial", 20))
    label_temp_J3.grid(column=2, row=6, sticky="n", pady=20,padx=5)

    label_temp_J4 = Label(master=frame_meteo, text="", fg="#FFFFFF", bg="#2eafff", font=("Arial", 20))
    label_temp_J4.grid(column=3, row=6, sticky="n", pady=20,padx=5)

    label_temp_J5 = Label(master=frame_meteo, text="", fg="#FFFFFF", bg="#2eafff", font=("Arial", 20))
    label_temp_J5.grid(column=4, row=6, sticky="n", pady=20,padx=5)
    
    return frame_meteo


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Prototype")
    app.iconbitmap("img/logo.ico")
    app.geometry("400x700")
    app.resizable(width=False, height=False)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)
    creer_meteo (app)
    

