import csv

def validate_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            dir_csv_reader = csv.DictReader(file)
            exprected_column = next(dir_csv_reader)
            for row in dir_csv_reader:
                if not float(row['Средний балл']) >= 0 and float(row['Средний балл' <= 5]) and exprected_column == len(row):
                    return 'Введенное значение некорректно'
                else:
                    return 'все чики пуки'
    except Exception as e:
        print(e)

path_p = r'C:\Users\kamin\PycharmProjects\PythonProject2\1stweek\students.csv'
print(validate_csv(path_p))