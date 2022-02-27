# --------------------------------------------------------2-------------------------------------------------------------
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)

my_list = [i ** 3 for i in range(1, 1001) if i % 2 != 0]

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

nums_seven = []
for number in my_list:
    item_sum = 0
    for item in str(number):
        item_sum += int(item)
    if item_sum % 7 == 0:
        nums_seven.append(number)

nums_seven_sum = 0
for number in nums_seven:
    nums_seven_sum += number
print(nums_seven_sum)


# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится
# нацело на 7.

added_seventeen = []
for i in my_list:
    new = i + 17
    added_seventeen.append(new)

nums_seventeen_seven = []
for number in added_seventeen:
    item_sum = 0
    for item in str(number):
        item_sum += int(item)
    if item_sum % 7 == 0:
        nums_seventeen_seven.append(number)

nums_seventeen_seven_sum = 0
for number in nums_seventeen_seven:
    nums_seventeen_seven_sum += number
print(nums_seventeen_seven_sum)
# print(sum(nums_seventeen_seven))
