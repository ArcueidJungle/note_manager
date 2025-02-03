import datetime

strin = input('введите строку ')

with open('file.txt', 'a') as file:
    file.write(str(datetime.datetime.now().date()) + ": " + strin + "\n")
