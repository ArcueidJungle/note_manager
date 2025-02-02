import random

num = random.randint(1, 100)
count = 0
while True:
    try:
        user_input = int(input('Введите число '))
    except ValueError:
        print('вы ввели не число')
        continue
    count += 1
    if user_input > num:
        print('число меньше введенного')
    elif user_input < num:
        print('число больше введенного')
    else:
        print('вы угадали число')
        break