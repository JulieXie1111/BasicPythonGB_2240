# ---------------------------------------------------------4------------------------------------------------------------
# * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.

full_name = ['Adam Jensen', 'Lucifer Morningstar', 'Bruce Wayne', 'Kate Kane']
l_names_letters = []
f_names_letters = []
res_dict = {}
for name in full_name:
    f_names_letters.append(name[0])
    for f in name.split(' ')[1]:
        if f.isupper():
            l_names_letters.append(f)

for i in l_names_letters:
    res_dict[i] = {x: y for x in f_names_letters for y in full_name if x == y[0]}

print(l_names_letters)
print(f_names_letters)

print(res_dict)
