username = input("Введите Имя пользователя: ")
title = [input("Введите Заголовок заметки: "),
         input("Введите Заголовок заметки: "),
         input("Введите Заголовок заметки: ")]
content = input("Введите описание заметки: ")
status =  input("Введите статус заметки(Открыта, Закрыта)")
created_date = input("Введите дату создания заметки в формате:(DD-MM-YYYY)")
issue_date = input("Введите дату истечения  заметки в формате:(DD-MM-YYYY)")
print("Имя пользователя: " + username)
print("Заголовки заметки: ")
print(title)
print("Описание заметки: " + content)
print("Cтатус заметки: " + status)
print("Дата создания: " + created_date)
print("Дата истечения заметки: " + issue_date )
