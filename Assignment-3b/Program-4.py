class TemperatureConverter:

    @staticmethod
    def celsiusToFahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheitToCelsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

if __name__ == "__main__":

    celsius_temp = 24
    fahrenheit_result = TemperatureConverter.celsiusToFahrenheit(celsius_temp)
    print(f"{celsius_temp}°C = {fahrenheit_result:.2f}°F")

    fahrenheit_temp = 94
    celsius_result = TemperatureConverter.fahrenheitToCelsius(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F = {celsius_result:.2f}°C")
