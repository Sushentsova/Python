import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes():
    """Makes n jokes"""
    n = int(input('Введите колличество шуток: '))
    for word in range(n):
        print(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')


get_jokes()


