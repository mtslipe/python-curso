# Exercício Python #014 - Conversor de Temperaturas
# formula: (0 °C × 9/5) + 32 = 32 °F



tempC = float(input("Informe a temperatura em °C: "))
tempF = ((tempC * 9) / 5) + 32

print(f"A temperatura de {tempC}°C corresponde a {tempF}°F!")
