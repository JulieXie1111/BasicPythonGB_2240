# ---------------------------------------------------3------------------------------------------------------------------
# Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А',
]


# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>).

def some_gen():
    for i in range(0, len(tutors)):
        if i < len(klasses):
            yield tutors[i], klasses[i]
        else:
            yield tutors[i], None


gen = some_gen()
print(type(gen))
print(*gen)

result_gen = ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None) for i in range(0, len(tutors)))
print(type(result_gen))
print(*result_gen)
