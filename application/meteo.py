from meteofrance_api import MeteoFranceClient
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import customtkinter as ctk
from tkinter import *




# ── API ───────────────────────────────────────────────────────────────────────

def API_meteo(nom_ville):
    client = MeteoFranceClient()
    places = client.search_places(nom_ville)

    if not places:
        return "Ville introuvable", None

    my_place = places[0]
    forecast = client.get_forecast_for_place(my_place)
    current_forecast = forecast.current_forecast

    if current_forecast:
        temp = current_forecast['T']['value']
        desc = current_forecast['weather']['icon']
        return f"{temp}°C", desc

    return "Données indisponibles", None


# ── Icône ─────────────────────────────────────────────────────────────────────
def get_icon_image(code, taille=100):

    # Si code est None ou vide, on met soleil par défaut
    if not code:
        icon_name = "erreur-404"
    else:
        # Enlève le "p" au début
        code_sans_p = code[1:]

        # Récupère le dernier caractère : "j" ou "n"
        jour_ou_nuit = code_sans_p[-1]

        # Enlève le dernier caractère
        milieu = code_sans_p[:-1]

        # Enlève "bis" ou "ter" s'il y en a
        if milieu.endswith("bis"):
            milieu = milieu[:-3]
        elif milieu.endswith("ter"):
            milieu = milieu[:-3]

        # Convertit le numéro
        numero = int(milieu)

        # Choix de l'icône
        if numero == 1 and jour_ou_nuit == "j":
            icon_name = "soleil"
        elif jour_ou_nuit == "n" and numero <= 4:
            icon_name = "pleine-lune"
        elif numero <= 4:
            icon_name = "nuageux"
        elif numero in range(16, 33):
            icon_name = "orage"
        elif numero in range(5, 12):
            icon_name = "pluvieux"
        else:
            icon_name = "pluie"

    chemin = f"img/meteo/{icon_name}.png"
    img = Image.open(chemin).resize((taille, taille))
    return ImageTk.PhotoImage(img)

# ── Actions ───────────────────────────────────────────────────────────────────

def afficher_valeur():
    valeur_saisie = ville_champ.get()

    affiche_ville.config(text=valeur_saisie.capitalize())
    label_resultat.config(text="Recherche en cours...")
    app.update()

    meteo_actuelle, icon = API_meteo(valeur_saisie)
    label_resultat.config(text=meteo_actuelle)

    try:
        img_object = get_icon_image(icon, taille=100)
        label_icon_jour.config(image=img_object)
        label_icon_jour.image = img_object  # référence obligatoire
    except Exception as e:
        print(f"Erreur de chargement de l'image : {e}")
        label_icon_jour.config(image="")
        label_icon_jour.image = None


# ── Interface ─────────────────────────────────────────────────────────────────

app = ctk.CTk()
app.title("Prototype")
app.iconbitmap("img/logo.ico")
app.geometry("400x700")
app.resizable(width=False, height=False)

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

frame_meteo = Frame(app, background="#2eafff")
frame_meteo.grid(row=0, column=0, sticky="nsew")
frame_meteo.grid_columnconfigure(0, weight=1)

affiche_ville = Label( master=frame_meteo, text="Entrez une ville",fg="#FFFFFF", bg="#2eafff",font=("Arial", 30, "bold"))
affiche_ville.grid(column=0, row=0, sticky="n", pady=(50, 20))

ville_champ = Entry(master=frame_meteo, bg="white", font=("Arial", 14), justify="center")
ville_champ.grid(column=0, row=1, sticky="n", pady=10)

bouton_valider = Button(master=frame_meteo, text="Rechercher", font=("Arial", 12), command=afficher_valeur)
bouton_valider.grid(column=0, row=2, sticky="n", pady=10)

label_icon_jour = Label(master=frame_meteo, image="", bg="#2eafff")
label_icon_jour.grid(column=0, row=3, sticky="n", pady=40)

label_resultat = Label(master=frame_meteo, text="", fg="#FFFFFF", bg="#2eafff", font=("Arial", 25))
label_resultat.grid(column=0, row=4, sticky="n", pady=40)

app.mainloop()
        print("--- MÉTÉO ACTUELLE ---")
        print(f"Température : {current_forecast['T']['value']} °C")
        print(f"Description : {current_forecast['weather']['desc']}")
        print(f"Humidité : {current_forecast['humidity']} %")
        print(f"Vent : {current_forecast['wind']['speed']} km/h\n")


    print("--- PRÉVISIONS QUOTIDIENNES ---")
    for day in forecast.daily_forecast[:3]:
        
        date = datetime.fromtimestamp(day['dt']).strftime('%d/%m/%Y')
        
        
        t_min = day.get('T', {}).get('min', 'N/A')
        t_max = day.get('T', {}).get('max', 'N/A')
        
        weather_12h = day.get('weather12H', {})
        desc = weather_12h.get('desc', 'Description non disponible')
        
        print(f"Le {date} -> Min: {t_min}°C, Max: {t_max}°C - {desc}")
    

def afficher_valeur():
    valeur_saisie = ville_champ.get()     
    affiche_ville.config(text=f" {valeur_saisie}")

#customtkinter
app = ctk.CTk()
app.title("Prototype")
app.geometry("400x700")
app.iconbitmap("img/logo.ico")

app.resizable(width=False,height=False)
app.grid_rowconfigure(0, weight=1)  # écran principal
app.grid_rowconfigure(1, weight=0)  # barre du bas
app.grid_columnconfigure(0, weight=1)    

frame_meteo = Frame(app,background="#2eafff")

frame_meteo.grid(row=0, column=0, sticky="nsew")

ville="Angers"
affiche_ville = Label(master=frame_meteo, text = ville, fg="#000000",bg="#2eafff",font=("Arial",10),justify=CENTER)
affiche_ville.grid(column=0,row=0,sticky="n")

ville_champ= Entry(master=frame_meteo, bg="white", font="Courier", textvariable =ville)
ville_champ.grid(column=0,row=1 ,sticky="n" )

bouton_valider = Button(master=frame_meteo, text="Valider", command=afficher_valeur)
bouton_valider.grid(column=0,row=2 ,sticky="n")


app.mainloop()


if __name__ == "__main__":
    print(ville)
