# ------------------------------------------------------2---------------------------------------------------------------
"""
 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
 вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
 завершиться с ошибкой.
"""


class ZeroDivision(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return 'ERROR: ZeroDivision\n {0}'.format(self.message) if self.message else 'ZeroDivision has been raised.'


while True:
    dividend = input('Enter first number(dividend): ')
    if dividend == 'q':
        break
    divisor = input('Enter second number(divisor): ')
    if divisor == 'q':
        break

    try:
        dividend = int(dividend)
        divisor = int(divisor)

        if divisor == 0:
            raise ZeroDivision("Can't divide by zero")

    except ValueError:
        print('You better enter a number not a string.')
    except ZeroDivision as err:
        print(err)
    else:
        print(f'Your result is {dividend / divisor}')


