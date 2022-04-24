# --------------------------------------------------------7-------------------------------------------------------------
"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата
"""


# Комплексное число — это выражение вида a + bi
# Сложение и вычитание происходят по правилу (a + bi) ± (c + di) = (a ± c) + (b ± d)i,
# а умножение — по правилу (a + bi) · (c + di) = (ac – bd) + (ad + bc)i (здесь как раз используется, что i2 = –1).
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.z = f'{self.a} + {self.b}i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        if self.a != 0:
            if self.b > 0:
                if self.b != 1:
                    return f'{self.a}+{self.b}i'
                else:
                    return f'{self.a}+i'
            elif self.b == 0:
                return f'{self.a}'
            else:
                return f'{self.a}{self.b}i'
        else:
            if self.b == 0:
                return f'0'
            else:
                return f'{self.b}i'


complex_num1 = ComplexNumber(10, -2)
complex_num2 = ComplexNumber(6, 3)
sum_complex = complex_num1 + complex_num2
print(sum_complex)
mult_complex = complex_num1 * complex_num2
print(mult_complex)
