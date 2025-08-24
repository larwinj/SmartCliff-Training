def get_max_min(temperatures, humidities):
    max_temp, min_temp, max_humid, min_humid = -51, 51, -1, 101
    for i in range(len(temperatures)):
        max_temp = max_temp if max_temp > temperatures[i] else temperatures[i]
        min_temp = min_temp if min_temp < temperatures[i] else temperatures[i]
        max_humid = max_humid if max_humid > humidities[i] else humidities[i]
        min_humid = min_humid if min_humid < humidities[i] else humidities[i]

    return max_temp, min_temp, max_humid, min_humid


def get_avg(temperatures, humidities):
    total_temp, total_humid = 0, 0
    n = len(temperatures)

    for i in range(n):
        total_temp += temperatures[i]
        total_humid += humidities[i]

    avg_temp = round(total_temp / n, 2)
    avg_humid = round(total_humid / n, 2)

    return avg_temp, avg_humid


def check_threshold(temperatures, humidities, temp_threshold, humid_threshold):
    exceeded = []
    n = len(temperatures)

    for i in range(n):
        if temperatures[i] > temp_threshold or humidities[i] > humid_threshold:
            exceeded.append((temperatures[i], humidities[i]))

    return exceeded


# ---- Main Execution ----
n = int(input("Enter number of readings: "))
temperatures = []
humidities = []

for i in range(n):
    temp, hum = map(int, input("Enter temperature and humidity: ").split())
    temperatures.append(temp)
    humidities.append(hum)

temp_threshold = int(input("Enter temperature threshold: "))
humid_threshold = int(input("Enter humidity threshold: "))

max_temp, min_temp, max_humid, min_humid = get_max_min(temperatures, humidities)
avg_temp, avg_humid = get_avg(temperatures, humidities)
exceeded_readings = check_threshold(temperatures, humidities, temp_threshold, humid_threshold)

print("Maximum temperature:", max_temp)
print("Minimum temperature:", min_temp)
print("Maximum humidity:", max_humid)
print("Minimum humidity:", min_humid)
print("Average temperature:", avg_temp)
print("Average humidity:", avg_humid)
print("Hourly readings exceeding threshold:")

for temp, hum in exceeded_readings:
    print("Temperature:", temp)
    print("Humidity:", hum)
