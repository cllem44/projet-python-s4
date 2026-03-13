from meteofrance_api import MeteoFranceClient
from datetime import datetime
import customtkinter as ctk
from tkinter import *


def API_meteo_test():
    # 1. Initialisation du client
    client = MeteoFranceClient()

   
    ville_recherchee = "Angers"
    places = client.search_places(ville_recherchee)
    
    if not places:
        print(f"Aucune ville trouvée pour {ville_recherchee}")
        return

    # On prend le premier résultat de la recherche
    my_place = places[0]
    print(f"Lieu sélectionné : {my_place.name} ({my_place.admin2}) - {my_place.country}\n")

    # 3. Récupération des prévisions météo pour ce lieu
    forecast = client.get_forecast_for_place(my_place)
    
    # Affichage des prévisions actuelles
    current_forecast = forecast.current_forecast
    if current_forecast:
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