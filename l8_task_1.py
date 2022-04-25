# ----------------------------------------------------------1-----------------------------------------------------------
"""Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение
ValueError. Пример:"""
import re


def email_parse(some_email):
    re_email = re.compile(r'^([a-z0-9_]+)@([a-z0-9.-]+\.[a-z]{2,})$')
    email_info = re_email.findall(some_email)
    # print(email_info)
    if email_info:
        name, domain = email_info[0]
        res_dict = {name: domain}
    else:
        raise ValueError(f'wrong email: {some_email}')
    return res_dict


print(email_parse('julie_carrey@icloud.com'))
print(email_parse('titovayulia96@yandex.ru'))
print(email_parse('crystal_x77@aliyun.cn'))
