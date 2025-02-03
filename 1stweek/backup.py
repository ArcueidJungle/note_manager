import datetime
import shutil

path = r'C:\Users\kamin\PycharmProjects\PythonProject2\1stweek\students.csv'
def backup_file(file_path):
    date = datetime.datetime.now().date()
    print(date)
    try:
        with open(f'{date}.bak', 'wb') as file:
            shutil.copy(file_path, f'{date}.bak')
        print(f"Backup created successfully on {date}")
    except Exception as e:
        print(e)

backup_file(path)