import sys

nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:      # ввели 2 числа
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    elif len(nums) == 0:  # если просто ввели имя модуля
        start_idx = 0
        end_idx = sum(1 for line in f)
    else:                 # ввели 2 числа
        start_idx = int(nums[0])
        end_idx = sum(1 for line in f)

    for idx, line in enumerate(f): # Номеруем строки. enumerate() начинает с нуля
        if start_idx <= idx + 1 <= end_idx: # поэтому +1
            print(line.strip())
