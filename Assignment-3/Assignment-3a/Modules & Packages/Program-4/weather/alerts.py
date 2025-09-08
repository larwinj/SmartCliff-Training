def check_alerts(temp_c, rain_chance):
    alerts = []
    if temp_c > 38:
        alerts.append("Heatwave Warning")
    if temp_c < 0:
        alerts.append("Cold Wave Warning")
    if rain_chance > 70:
        alerts.append("Heavy Rain Warning")
    if not alerts:
        alerts.append("No extreme weather alerts")
    return alerts
