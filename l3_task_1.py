# --------------------------------------------------------1-------------------------------------------------------------
# Написать функцию num_translate(), переводящую числительные от 0 до 10 с английского на русский язык.
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
# перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(num):
    """Function, that Translates numbers from 1 to 10 from English into Russian."""
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
    translation = tr_dict.get(num, 'there is no such a word in my dictionary.')
    print(translation)


num_translate('three')
