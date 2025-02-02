from datetime import datetime

# проверка ввода делается через ловлю ошибки
# если все правильно то возвращаем дату и идем дальше, если вылазит ошибка ValueError то выводим сообщение об ошибке и начинаем цикл заново
def get_issue_date():
    while True:
        issue_date_input = input('Введите дату дедлайна (в формате день-месяц-год): ')
        try:
            issue_date = datetime.strptime(issue_date_input, '%d-%m-%Y')
            return issue_date
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год.")

# получаем текущую дату
def get_current_date():
    return datetime.now()

# функция для подсчета и вывода string о состоянии дедлайна.
# условный оператор, где мы сравнивание текущую дату с датой дедлайна если truе то
# выводим дни до дедлайна если false то оповещаем о прошедшем дедлайне
def calculating_day_dif(issue_date):
    current_date = get_current_date()
    if (issue_date < current_date):
        days_diff = (current_date - issue_date).days
        return  (f"До дедлайна {days_diff} дней")
    else:
        return ('Дедлайн прошел')

#Основная часть программы
issue_day = get_issue_date()
result = calculating_day_dif(issue_day)
print(result)
#пиздец