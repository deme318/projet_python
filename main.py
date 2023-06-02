import network
from m5stack import lcd
import urequests as requests
import json

# Configuration de l'écran M5Stack
lcd.clear()
lcd.font(lcd.FONT_Default)

# Définition des couleurs
WHITE = lcd.WHITE
BLACK = lcd.BLACK

# Définition du fond en noir
lcd.clear(BLACK)

# Clé d'API OpenWeatherMap (remplacez par votre propre clé)
api_key = "610aa637f7a68197d131682923e2da75"

# Récupération et affichage des données météorologiques pour chaque ville
villes = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice"]
for ville in villes:
    url = "http://api.openweathermap.org/data/2.5/weather?q={ville},fr&appid={api_key}&units=metric"
    response = requests.get(url.format(ville=ville, api_key=api_key))
    data = json.loads(response.text)

    # Extraction des informations pertinentes
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    # Affichage des informations sur l'écran M5Stack
    lcd.print(ville, lcd.CENTER, 10, color=WHITE)
    lcd.print("Température: {}°C".format(temperature), lcd.CENTER, 40, color=WHITE)
    lcd.print("Description: {}".format(description), lcd.CENTER, 60, color=WHITE)
    lcd.print("", lcd.CENTER, 80, color=WHITE)  # Ligne vide pour l'espace entre les villes

# Attente avant de fermer l'écran
input("Appuyez sur une touche pour fermer l'écran...")
lcd.clear()
