try:
    digit = int(input('Введите число '))
except ValueError:
    print('Вы ввели не число')

if digit > 0 and digit % 2 == 0:
    print('число положительное и четное')
elif digit < 0 and digit % 2 != 0:
    print('число отрицательное и нечетное')
elif digit == 0:
    print('число равно 0')
else:
    print("Число не соответствует заданным условиям")
