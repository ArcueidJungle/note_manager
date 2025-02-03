import csv
from pathlib import Path

file_path = Path(r"C:\Users\kamin\PycharmProjects\PythonProject2\1stweek\students.csv")

try:
    with open(file_path, 'r', encoding= 'utf-8') as file:
        print('Содержимое файла')
        print(file.read())
        file.seek(0)
        reader = csv.DictReader(file, delimiter= ',')
        print('\n данные студентов')
        for row in reader:
            print(f"Имя: {row['Имя']}, Балл: {row['Средний балл']}")
        maxim = [min(int(row['Средний балл'])) for row in  reader]
        print(maxim)
except FileNotFoundError:
    print('Такого файла не существует')
except UnicodeDecodeError:
    print('Ошибка кодировки')
except Exception as e:
    print(f'Произошла ошибка {e}')