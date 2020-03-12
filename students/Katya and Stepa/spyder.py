import requests  # импортируем модуль
f = open(r'D:\file.pdf', "wb")  # открываем файл для записи, в режиме wb
ufr = requests.get("https://spbau.ru/assets/documents/бакалавры и магистры/timetables/bakalavriat_2_semestr_2019-2020.pdf")  # делаем запрос
f.write(ufr.content)  # записываем содержимое в файл; как видите - content запроса
f.close()