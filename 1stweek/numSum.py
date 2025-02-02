try:
    digit = int(input('Введите число '))
except ValueError:
    print('Вы ввели не число')

summary = 0
if digit < 0:
    print('число должно быть неотрицательным')
else:
    for i in range(1, digit + 1):
        summary = summary + i
    print(f"Сумма чисел от 1 до {digit} : {summary}")
