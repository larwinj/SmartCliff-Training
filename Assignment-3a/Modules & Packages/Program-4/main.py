from weather import get_forecast, c_to_f, check_alerts

def main():
    city = input("Enter city: ")

    forecast = get_forecast(city)
    temp_c = forecast["temperature_c"]
    temp_f = c_to_f(temp_c)
    rain = forecast["rain_chance"]

    print(f"\nCity: {city}")
    print(f"Temperature: {temp_c}°C ({temp_f}°F)")
    print(f"Rain chance: {rain}%")

    # Print alerts
    alerts = check_alerts(temp_c, rain)
    for alert in alerts:
        print("ALERT:", alert)


if __name__ == "__main__":
    main()
