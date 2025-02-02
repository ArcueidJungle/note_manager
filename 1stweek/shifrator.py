user_input = input('Введите строку для шифрования')

cahrinput = list(user_input)
cahrinput2 = [chr(ord(x) + 1)  for x in cahrinput]
strin = ''.join(cahrinput2)
print(strin)