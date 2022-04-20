# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, date):  # dd-mm-yyyy
        self.date = date

    @classmethod
    def str_to_int(cls, date):
        res = list(map(int, date.split('-')))

        return res

    # @staticmethod
    # def date_val(data):
    #     re_date = re.compile(r"^(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](19|20)\d\d$")
    #     if re_date.match(data):
    #         print('OK')
    #     else:
    #         print('not OK')
    @staticmethod
    def validation(res):
        day, month, year = res
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 9999 >= year >= 0:
                    return f'All right'
                else:
                    return f'{year} - wrong year'
            else:
                return f'{month} -  wrong month'
        else:
            return f'{day} - wrong day'


print(Data.validation(Data.str_to_int("20-02-2002")))
print(Data.validation(Data.str_to_int("29-05-1996")))
print(Data.validation(Data.str_to_int("45-02-2022")))
