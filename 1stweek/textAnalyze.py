import string

stri = input('введите любую строку ')
stri4 = stri.strip().split()
stri3 = stri.replace(" ", '')
stri2 = stri.lower().strip().split()

# Удаляем знаки препинания из каждого слова
table = str.maketrans("", "", string.punctuation)
stri2 = [word.translate(table) for word in stri2]  # Сохраняем результат

print(len(stri3))  # Длина строки без пробелов
print(stri4[::-1])  # Список слов в обратном порядке
print(len(set(stri2)))  # Количество уникальных слов