
def celsius_to_fahrenheit(temp_c):
    return round(temp_c * 9/5 + 32, 2)

try:
    temperature_c = float(input('введите температуры в цельсиях'))
    print(f'{(celsius_to_fahrenheit(temperature_c))}°F')
except ValueError:
    print("Ошибка: введите число, например, 25 или -3.5.")

