# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?



def get_jokes():
     from random import choice

     nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
     adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
     adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
     result_jokes = (choice(nouns), choice(adverbs), choice(adjectives))

     temp_jokes = ''
     for item in result_jokes:
        temp_jokes += item
        temp_jokes += ' '

        print(temp_jokes)

get_jokes()


