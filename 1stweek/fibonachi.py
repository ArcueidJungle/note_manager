def fibonacci(s):
    listed = [0, 1]
    for i in range(2, s):
        listed.append(listed[i - 1] + listed[i - 2])
    return list

try:
    digit = int(input('введите сколько чисел фибоначи'))
    if digit < 1:
        print('[0]')
    else:
        print(fibonacci(digit))
except ValueError:
    print('введите целое число')


