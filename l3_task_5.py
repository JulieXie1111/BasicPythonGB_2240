# --------------------------------------------------------5-------------------------------------------------------------
from random import choice


# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
# (по одному из каждого):
def get_jokes(n, no_repetition=False):
    """""A function that returns n jokes formed from three random words taken from three lists (one from each)"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result_jokes = []
    i = 0
    # max_jokes = min(len(nouns), len(adverbs), len(adjectives))  # предотвращает ошибку, если не разрешен повтор.
    while i < n:
        rand_noun = choice(nouns)
        rand_adv = choice(adverbs)
        rand_adj = choice(adjectives)
        joke = f"{rand_noun} {rand_adv} {rand_adj}"
        result_jokes.append(joke)
        if no_repetition:  # флажок
            nouns.remove(rand_noun)
            adverbs.remove(rand_adv)
            adjectives.remove(rand_adj)
            if not nouns or not adverbs or not adjectives:
                break
        i += 1

    print(result_jokes)


get_jokes(6)
get_jokes(10, no_repetition=True)
