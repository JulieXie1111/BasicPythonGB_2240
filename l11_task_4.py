# ----------------------------------------------------------------------------------------------------------------------
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
"""
# ----------------------------------------------------------------------------------------------------------------------
"""
5.Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу 
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь).
"""
# ----------------------------------------------------------------------------------------------------------------------
"""
6.Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для 
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

# ----------------------------------------------------------------------------------------------------------------------
import re


class WrongSerialNum(Exception):
    def __init__(self, txt):
        self.txt = txt if txt else None

    def __str__(self):
        return f'Error: WrongSerialNum\n {self.txt}' if self.txt else 'Error: WrongSerialNum'


class Warehouse:
    """Учет всей техники ведется по серийным номерам"""
    storage = {'printers': [], 'scanners': [], 'copiers': []}

    all_stored_serial_nums = []
    printer_amount = 0
    copier_amount = 0
    scanner_amount = 0
    equipment_amount = 0

    @classmethod
    def goes_in(cls, equipment):
        if isinstance(equipment, Printer):
            try:
                if equipment.serial_number in cls.all_stored_serial_nums:
                    raise WrongSerialNum('This equipment already exists.')
            except WrongSerialNum as err:
                print(err)
            else:
                cls.storage['printers'].append({equipment.serial_number: equipment.__dict__})
                cls.all_stored_serial_nums.append(equipment.serial_number)
                cls.equipment_amount += 1
                cls.printer_amount += 1
        if isinstance(equipment, Scanner):
            try:
                if equipment.serial_number in cls.all_stored_serial_nums:
                    raise WrongSerialNum('This equipment already exists.')
            except WrongSerialNum as err:
                print(err)
            else:
                cls.storage['scanners'].append({equipment.serial_number: equipment.__dict__})
                cls.all_stored_serial_nums.append(equipment.serial_number)
                cls.equipment_amount += 1
                cls.scanner_amount += 1
        if isinstance(equipment, Copier):
            try:
                if equipment.serial_number in cls.all_stored_serial_nums:
                    raise WrongSerialNum('This equipment already exists.')
            except WrongSerialNum as err:
                print(err)
            else:
                cls.storage['copiers'].append({equipment.serial_number: equipment.__dict__})
                cls.all_stored_serial_nums.append(equipment.serial_number)
                cls.equipment_amount += 1
                cls.copier_amount += 1

    @classmethod
    def goes_out(cls, equipment):
        if equipment.__class__ == Printer:
            cls.all_stored_serial_nums.remove(equipment.serial_number)
            cls.equipment_amount -= 1
            cls.printer_amount -= 1
            for el in cls.storage['printers']:
                if equipment.serial_number in el:
                    cls.storage['printers'].remove(el)
            print(f'{equipment.model} is out. ')

        if equipment.__class__ == Scanner:
            cls.all_stored_serial_nums.remove(equipment.serial_number)
            cls.equipment_amount -= 1
            cls.printer_amount -= 1
            for el in cls.storage['scanners']:
                if equipment.serial_number in el:
                    cls.storage['scanners'].remove(el)
            print(f'{equipment.model} is out. ')

        if equipment.__class__ == Copier:
            cls.all_stored_serial_nums.remove(equipment.serial_number)
            cls.equipment_amount -= 1
            cls.printer_amount -= 1
            for el in cls.storage['copiers']:
                if equipment.serial_number in el:
                    cls.storage['copiers'].remove(el)
            print(f'{equipment.model} is out. ')


class OfficeEquipment:

    def __init__(self, model, color, serial_number):
        self.model = model
        self.color = color
        try:
            if OfficeEquipment.validate_serial(serial_number):
                self.serial_number = serial_number

            else:
                raise WrongSerialNum('Serial number is incorrect')
        except WrongSerialNum as err:
            print(err)

    def __str__(self):
        return f"Info:\n Model: {self.model}\nColor: {self.color}\nSerial number: {self.serial_number}"

    @staticmethod
    def validate_serial(arg):
        """Проверка серийного номера"""

        re_serial = re.compile(r'^[A-Z]{4}[0-9]{4}$')
        if re_serial.match(arg):
            return bool(re_serial.match(arg))


class Printer(OfficeEquipment):
    p = 0

    def __init__(self, model, color, serial_number, print_technology, print_speed):
        super().__init__(model, color, serial_number)
        self.print_technology = print_technology
        self.print_speed = int(print_speed)
        Printer.p += 1

    def get_amount_p(self):
        return self.p

    def __str__(self):
        return f"Info:\nModel: {self.model}\nColor: {self.color}\nSerial number: {self.serial_number}\n" \
               f"Print technology: {self.print_technology}\nPrint speed: {self.print_speed}"


class Scanner(OfficeEquipment):
    s = 0

    def __init__(self, model, color, serial_number, scan_technology, scanner_type):
        super().__init__(model, color, serial_number)
        self.scan_technology = scan_technology
        self.scanner_type = scanner_type
        Scanner.s += 1

    def __str__(self):
        return f"Info:\nModel: {self.model}\nColor: {self.color}\nSerial number: {self.serial_number}\n" \
               f"Scan technology: {self.scan_technology}\nScanner type: {self.scanner_type}"


class Copier(OfficeEquipment):
    c = 0

    def __init__(self, model, color, serial_number, copy_speed):
        super().__init__(model, color, serial_number)
        self.copy_speed = int(copy_speed)
        Copier.c += 1

    def __str__(self):
        return f"Info:\nModel: {self.model}\nColor: {self.color}\nSerial number: {self.serial_number}\n" \
               f"Copy speed: {self.copy_speed}"


print(Warehouse.equipment_amount, Warehouse.printer_amount, Warehouse.scanner_amount, Warehouse.copier_amount,
      Warehouse.storage, sep='\n')
printer1 = Printer("HP DeskJet 2710e", 'white', 'FGHK2582', 'inkjet', 25)
printer2 = Printer("EPSON 800", 'black', 'JING1101', 'laser', 22)
scanner1 = Scanner('HP ScanJet Pro 2500 f1', 'white', 'QWER8546', 'CMOS CIS', 'Flatbed')
copier1 = Copier('Panasonic T8100', 'pink', 'COUR4569', 22)
Warehouse.goes_in(printer1)
Warehouse.goes_in(scanner1)
Warehouse.goes_in(copier1)
Warehouse.goes_in(printer2)
print(Warehouse.storage)
print('X' * 250)
print(Warehouse.equipment_amount, Warehouse.printer_amount, Warehouse.scanner_amount, Warehouse.copier_amount,
      Warehouse.storage, sep='\n')
Warehouse.goes_out(printer1)
Warehouse.goes_out(copier1)
print('X' * 250)
print(Warehouse.equipment_amount, Warehouse.printer_amount, Warehouse.scanner_amount, Warehouse.copier_amount,
      Warehouse.storage, sep='\n')
