# ---------------------------------------------------------5------------------------------------------------------------
"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра
"""


class Stationery:
    """Канцелярская принадлежность"""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Я пишу ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Я рисую карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Я все пачкаю с {self.title}')


some_pen = Pen('Pilot')
some_pen.draw()

some_pencil = Pencil('Faber_Castell')
some_pencil.draw()

some_handle = Handle('Berlingo')
some_handle.draw()
