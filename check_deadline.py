from datetime import datetime

# проверка ввода делается через ловлю ошибки
# если все правильно то цикл прерывается и идет дальше, если вылазит ошибка ValueError то выводим сообщение об ошибке и начинаем цикл заново
while True:
    issue_date_input = input('Введите дату дедлайна (в формате день-месяц-год): ')
    try:
        issue_date = datetime.strptime(issue_date_input, '%d-%m-%Y')
        break
    except ValueError:
        print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")

# условный оператор, где мы сравнивание текущую дату с датой дедлайна если truе то
# выводим дни до дедлайна если false то оповещаем о прошедшем дедлайне
if issue_date < (current_date:= datetime.now()):
    days_diff = (current_date - issue_date).days
    print(f"До дедлайна {days_diff} дней")
else:
    print('Дедлайн прошел')