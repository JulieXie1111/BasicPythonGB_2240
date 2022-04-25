# ---------------------------------------------------------2-------------------------------------------------------------
# (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.

def num_translate_adv(num):
    tr_dict = {'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}
    if num.istitle():
        result = tr_dict.get(num.lower(), 'there is no such a word').title()
    else:
        result = tr_dict.get(num, 'there is no such a word')

    print(result)


num_translate_adv('Three')
