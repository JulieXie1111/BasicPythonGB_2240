"""
3.  Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем
очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
этом работа скрипта не должна завершаться.
"""


class ElementError(Exception):
    def __init__(self, el):
        self.message = el if el else None

    def __str__(self):
        return f'Error: ElementError\n {self.message}' if self.message else 'Error: ElementError'


user_list = []


def get_num(x):
    if x[0] in '+-':
        return x[1:]


while True:
    user_inp = input('Enter a number: ')
    if user_inp == 'stop':
        break
    try:
        if user_inp.isdigit() or get_num(user_inp):
            user_list.append(int(user_inp))
        else:
            raise ElementError('Your number must be a digit.')
    except ElementError as e:
        print(e)
    else:
        print(f"Your number {user_inp} has been added to the list")

print(user_list)
