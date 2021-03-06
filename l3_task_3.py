# ------------------------------------------------------3---------------------------------------------------------------
# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


def thesaurus(*args):
    initials = (el[0] for el in args)  # Генератор первых букв.
    res_dict = {}
    for i in initials:
        res_dict[i] = [name for name in args if name[0] == i]
    return res_dict


a = thesaurus('Rachel', 'Phoebe', 'Joey', 'Monica', 'Chandler', "Ross")
print(a)

# Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

# Отсортировать словарь по ключам сам по себе нельзя, но можно создать список, содержащий его ключи, и отсортировать
# его. В цикле for перебрать элементы списка, используя элемент списка как ключ словаря:

a_list = list(a.keys())
a_list.sort()
for j in a_list:
    print(f'{j} -- {a[j]}')


# ---------------------------------------------------вариант решения----------------------------------------------------

def thesaurus(*names):
    out_dict = {}
    for name in names:
        out_dict.setdefault(name[0], []).append(name)
    return out_dict


print(thesaurus('Rachel', 'Phoebe', 'Joey', 'Monica', 'Chandler', "Ross"))

