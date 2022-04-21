# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:

    def __init__(self):
        self.date = None

    def set_date(self, date):
        if Data.validation(Data.str_to_int(date)):
            self.date = date

    @classmethod
    def str_to_int(cls, date):
        res = list(map(int, date.split('-')))

        return res

    @staticmethod
    def validation(res):
        day, month, year = res
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 9999 >= year >= 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


print(Data.validation(Data.str_to_int("20-02-2002")))
print(Data.validation(Data.str_to_int("29-05-1996")))
print(Data.validation(Data.str_to_int("45-02-2022")))
print()
today = Data()
today.set_date("21-04-2022")
print(today.date)
print()
a = Data()
a.set_date("45-02-2022")
print(a.date)
