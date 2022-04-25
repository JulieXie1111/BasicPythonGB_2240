# -------------------------------------------------------3--------------------------------------------------------------
# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при
# хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
import json
import sys

user_dict = {}
with open('users.csv', 'r', encoding='utf-8') as f1:
    with open('hobby.csv', 'r', encoding='utf-8') as f2:
        num_lines_users = sum(1 for line in f1)
        num_lines_hobby = sum(1 for line in f2)

        f1.seek(0)
        f2.seek(0)

        if num_lines_users < num_lines_hobby:
            sys.exit(1)
        else:
            for line1 in f1:
                line2 = f2.readline().strip()
                user_dict[line1.strip()] = line2 if line2 is not None else line2

print(user_dict)

with open('user_hobby.json', 'w', encoding='utf-8') as f:
    json.dump(user_dict, f, ensure_ascii=False)

with open('user_hobby.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

print(content)
