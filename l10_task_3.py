class Cell:
    def __init__(self, nums):
        self.nums = nums  # 13

    def make_order(self, rows):  # 5
        return '\n'.join(['O' * rows for _ in range(self.nums // rows)]) + '\n' + 'O' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print("Sum of cell is: ")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Subtraction of cell is: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше,чем во второй. Вычитание невозможно!'

cells = Cell(50)
print(cells.make_order(10))
