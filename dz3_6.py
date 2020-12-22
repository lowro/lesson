def func(text):
    def int_func(word: str):
        return f'{word[0].upper()}{word[1:]}'
    words = text.split()
    return ' '.join(list(map(lambda word: int_func(word), words)))
print(func('ПрОверка работы'))