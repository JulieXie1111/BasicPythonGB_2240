# ----------------------------------------------------------4-----------------------------------------------------------
"""
Реализуйте базовый класс Car.
У класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    """Базовый класс Car"""

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going!')

    def stop(self):
        print(f'{self.name} has stopped.')

    def direction(self, direction):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f"{self.name}`s speed is {self.speed}.")


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name}: current speed {self.speed}. Speeding!'
              if self.speed > 60 else f"{self.name}: speed {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name}: current speed {self.speed}. Speeding!'
              if self.speed > 40 else f"{self.name}: speed {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(70, 'red', 'Lexus')
print(car_1.name)
car_1.go()
car_1.stop()
car_1.show_speed()
car_2 = WorkCar(50, 'blue', 'Kamaz')
print(car_2.name)
car_2.go()
car_2.stop()
(car_2.show_speed())
car_3 = SportCar(80, 'yellow', 'Lamborghini')
print(car_3.name)
car_3.go()
car_3.stop()
(car_3.show_speed())
car_4 = PoliceCar(90, 'white', 'Police car')
print(car_1.name)
car_4.go()
car_4.direction('right')
car_4.stop()
car_4.direction('left')
(car_4.show_speed())
