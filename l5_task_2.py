# ----------------------------------------------------2-----------------------------------------------------------------
# (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield
n = int(input("Input number: "))
odd_nums_gen = (num for num in range(1, n + 1, 2))
print(*odd_nums_gen)


# ---------------------------------------------вариант решения---------------------------------------------------------
def odd_nums_gen(num_max):
    odd_nums = (num for num in range(1, num_max + 1, 2))
    return odd_nums


odds = odd_nums_gen(15)
print(next(odds))
print(type(odds))
print(*odds)
