
def c_to_F(temp_c):
    return round(temp_c * 9/5 + 32, 3)


try:
    temperature_c = float(input('введите температуры в цельсиях'))
    print(str(c_to_F(temperature_c)) + '°F')
except ValueError:
    print('Ошибка')

