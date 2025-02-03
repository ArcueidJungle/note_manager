import csv
import json
import pathlib

def csv_to_json(path_file : str):
    file_path = pathlib.Path(path_file)
    file_path_withsuf = file_path.with_suffix('.json')
    try:
        with open(path_file, 'r', encoding = 'utf-8') as file_csv:
            dict_reader = csv.DictReader(file_csv)
            data = [row for row in dict_reader]

        with open(file_path_withsuf, 'w', encoding = 'utf-8') as file_json:
            json.dump(data, file_json, indent = 4, ensure_ascii= False)
        print(f'файл{path_file} успешно конвертирован')
    except Exception as e:
        print(e)

file_path = r'C:\Users\kamin\PycharmProjects\PythonProject2\1stweek\students.csv'
csv_to_json(file_path)