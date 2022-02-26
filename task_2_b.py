# Выполнить задание не создавая список*


my_list = [i ** 3 for i in range(1, 1001) if i % 2 != 0]

nums_seven_sum = 0
for number in my_list:
    item_sum = 0
    for item in str(number):
        item_sum += int(item)
    if item_sum % 7 == 0:
        nums_seven_sum += number

print(nums_seven_sum)

nums_seventeen_seven_sum = 0
for number in my_list:
    number += 17
    item_sum = 0
    for item in str(number):
        item_sum += int(item)
    if item_sum % 7 == 0:
        nums_seventeen_seven_sum += int(number)

print(nums_seventeen_seven_sum)
