first = '1 выполнено'
second = '2 в процессе'
third = "3 отложено"
status = second
while True:
    print("Текущий статус заметки:" + status[2:])
    status_num = input("Выберите новый статус заметки:\n"
                       "1 выполнено \n"
                       "2 в процессе \n"
                       "3 отложено\n"
                       "Напишите exit для выхода из редактирования статуса заявки\n")
    if status_num == '1' or status_num == 'выполнено':
        status = first
    elif status_num == '2' or status_num == 'в процессе':
        status = second
    elif status_num == '3' or status_num == 'отложено':
        status = third
    elif status_num == 'exit':
        break
    else:
        print("некорректный ввод")
print("Редактирование статуса заявки завершенно")
