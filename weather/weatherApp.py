
import pyowm
from configi.config_reader import ConfigReader

class WeatherInformation():
    def __init__(self):
        self.config_reader = ConfigReader()
        self.configuration = self.config_reader.read_config()
        self.owmapikey = self.configuration['WEATHER_API_KEY']
        self.owm = pyowm.OWM(self.owmapikey)

    def get_weather_info(self,city):
        self.city=city

        observation = self.owm.weather_at_place(city)
        w = observation.get_weather()
        latlon_res = observation.get_location()
        lat = str(latlon_res.get_lat())
        lon = str(latlon_res.get_lon())

        wind_res = w.get_wind()
        wind_speed = str(wind_res.get('speed'))

        humidity = str(w.get_humidity())

        celsius_result = w.get_temperature('celsius')
        temp_min_celsius = str(celsius_result.get('temp_min'))
        temp_max_celsius = str(celsius_result.get('temp_max'))

        fahrenheit_result = w.get_temperature('fahrenheit')
        temp_min_fahrenheit = str(fahrenheit_result.get('temp_min'))
        temp_max_fahrenheit = str(fahrenheit_result.get('temp_max'))
        self.bot_says = "Hoy día el clima en " + city +" es :\n Maxima Temperatura - "+temp_max_celsius+ " Grados Celcius"+".\n Temperatura Minima - "+temp_min_celsius+ " Grados Celcius" +". \n" + "Humedad - " + humidity + "%"
        return self.bot_says