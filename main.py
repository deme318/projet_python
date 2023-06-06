from m5stack import lcd, btnA, btnB, btnC
import urequests as requests
import json

class WeatherApp:
    def __init__(self):
        # Configuration de l'écran M5Stack
        lcd.clear()
        lcd.font(lcd.FONT_Default)

        # Définition des couleurs
        self.WHITE = lcd.WHITE
        self.BLACK = lcd.BLACK

        # Définition du fond en noir
        lcd.clear(self.BLACK)

        # Clé d'API OpenWeatherMap
        self.api_key = "610aa637f7a68197d131682923e2da75"

        # Liste des villes
        self.villes = [
            "Paris", "Marseille", "Lyon", "Toulouse", "Nice",
            "Nantes", "Strasbourg", "Montpellier", "Bordeaux",
            "Lille", "Rennes", "Reims", "Saint-Étienne", "La Rochelle",
            "Angers", "Grenoble"
        ]

        # Index de la ville sélectionnée
        self.selected_index = 0

    def update_weather_data(self, ville):
        url = "http://api.openweathermap.org/data/2.5/weather?q={},fr&appid={}&units=metric".format(ville, self.api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        # Extraction des informations pertinentes
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        # Nettoyage de l'écran
        lcd.clear(self.BLACK)

        # Affichage de la liste des villes
        for i in self.villes:
            color = self.WHITE if i == self.selected_index else self.BLACK
            lcd.print(i * 20, color=color)

        # Affichage des informations sur l'écran M5Stack
        lcd.print("Ville: {}".format(ville), lcd.CENTER, 10, color=self.WHITE)
        lcd.print("Temperature: {}°C".format(temperature), lcd.CENTER, 40, color=self.WHITE)
        lcd.print("Humidite: {}%".format(humidity), lcd.CENTER, 60, color=self.WHITE)
        lcd.print("Vitesse du vent: {} m/s".format(wind_speed), lcd.CENTER, 80, color=self.WHITE)
        lcd.print("Description: {}".format(description), lcd.CENTER, 100, color=self.WHITE)

    def run(self):
        while True:
            # Vérification du bouton de sélection
            if btnA.wasPressed():
                ville = self.villes[self.selected_index]
                self.update_weather_data(ville)

            # Vérification du bouton d'annulation
            if btnB.wasPressed():
                lcd.clear(self.BLACK)

            # Vérification du bouton de la ville suivante
            if btnC.wasPressed():
                self.selected_index = (self.selected_index + 1) % len(self.villes)
                ville = self.villes[self.selected_index]
                self.update_weather_data(ville)

        lcd.clear()

# Instanciation de l'application météo
app = WeatherApp()

# Lancement de l'application
app.run()
