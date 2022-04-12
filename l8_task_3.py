# --------------------------------------------------------3-------------------------------------------------------------

# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете
# ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
from functools import wraps


def type_loger(function_to_decorate):
    @wraps(function_to_decorate)
    def wrapper(*args):
        for arg in args:
            print(f'{function_to_decorate.__name__}({arg}:{type(arg)})', end=', ')
        return function_to_decorate(*args)

    return wrapper


@type_loger
def calc_cube(*args):
    results = []
    for number in args:
        results.append(number ** 3)
    print(results)


calc_cube(5, 2, 3)
