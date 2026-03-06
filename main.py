"""from meteofrance_api import MeteoFranceClient
from datetime import datetime

def main():
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
    

   

if __name__ == "__main__":
    main()"""


import customtkinter as ctk
from tkinter import *
# Faire que lorsque qu'on appuie une première fois sur le bouton quitter, ça éteigne l'ecran en affichant un ecran noir surement avec ctk.set_appearance_mode("dark") comme commande

def Eteindretelephone():
    canvas.pack(fill="both", expand=True)

def Ecranaccueil():
    canvas.pack_forget()
def app_meteo():
    canvas
#customtkinter
app = ctk.CTk()
app.title("Prototype")
app.geometry("400x700")
app.resizable(width=False,height=False)
frame_ecran = Frame(app)
frame_ecran.pack(fill="both", expand=True)
barre_bas = Frame(app, height=60, bg="#c1c1c1")
barre_bas.pack(fill="x", side="bottom")
#tkinter
canvas = Canvas(frame_ecran, bg="black") 
#fill="both" : prend largeur + hauteur
#expand=True : utilise tout l’espace disponible

buttoneteindre = ctk.CTkButton(master=barre_bas,text="Eteindre",command=Eteindretelephone,width=80,height=40,border_width=0,corner_radius=4,hover=False)
buttoneteindre.pack(side="bottom")
buttonprincipale = ctk.CTkButton(master=barre_bas,text="",command=Ecranaccueil,width=55,height=55,border_width=0,corner_radius=30,hover=False)
buttonprincipale.pack(side="bottom")
app.mainloop()