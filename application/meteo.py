from meteofrance_api import MeteoFranceClient
from datetime import datetime

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
    

   

if __name__ == "__main__":
    API_meteo_test()