# -------------------------------------------------------2--------------------------------------------------------------
# Дан список. Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
# до двух целочисленных разрядов.

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def get_sign(x):
    """Достает + или - из строки."""
    if x[0] in "+-":
        return x[0]


idx = 0
while idx < len(some_list):
    sign = get_sign(some_list[idx])
    if some_list[idx].isdigit() or sign and some_list[idx][1:].isdigit():
        if sign:
            some_list[idx] = sign + some_list[idx][1:].zfill(2)
        else:
            some_list[idx] = some_list[idx].zfill(2)
        some_list.insert(idx, '"')
        some_list.insert(idx + 2, '"')
        idx += 2
    idx += 1

print(' '.join(some_list))

# новый список не создавался.
