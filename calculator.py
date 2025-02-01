

def is_operator(opreraton):
    return opreraton in ('+', '-', '/', '*')

def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == '*':
        return  first * second
    else:
        if second == 0:
            return ('деление на 0 недопустимо')
        return first / second


def main():
    try:
        first = float(input('Введите первое число'))
        second = float(input('Введите второе число'))
    except:
        print('Некорректное значение')
    operation = input('Введите операцию (+, -, *, /):')

    if is_operator(operation):
        print(calc(first, second, operation))
    else:
        print('неправильный оператор')


if __name__ == '__main__':
    main()