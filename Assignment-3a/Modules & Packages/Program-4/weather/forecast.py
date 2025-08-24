import random

def get_forecast(city):
    temperature_c = random.randint(-5, 45)
    rain_chance = random.randint(0, 100)
    return {"city": city, "temperature_c": temperature_c, "rain_chance": rain_chance}
