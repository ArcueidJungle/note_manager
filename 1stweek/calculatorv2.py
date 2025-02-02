import sys


def get_numbers():
    while True:
        try:
            vallue1 = int(input('введите первое число'))
            vallue2 = int(input('введите второе число'))
            return vallue1, vallue2
        except ValueError:
            print('вы ввели не число')

def get_operation():
    while True:
        sign_input = input('введите оператор')
        if sign_input not in ('+', '-', '/', '*'):
            print('вы ввели не оператор')
        else:
            return sign_input


def calculate(a, b, op):
    while True:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return 'На 0 делить нельзя'
            return a / b
        else:
            return 'неизвестная ошибка'

a , b = get_numbers()
print(calculate(a, b, get_operation()))