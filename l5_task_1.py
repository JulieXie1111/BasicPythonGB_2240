# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.

def odd_nums(n):
    for num in range(1, n + 1, 2):
        yield num


nums_odd = odd_nums(15)
print(next(nums_odd))
print(next(nums_odd))
print(next(nums_odd))
print(next(nums_odd))