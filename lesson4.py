from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


text = """В заросшем парке стоит старинный дом
Забиты окна и мрак царит из вечно в нем
Сказать я пытался чудовищ нет на Земле
Но тут же раздался ужасный голос во мгле
Голос во мгле
Мне больно видеть белый свет
Мне лучше в полной темноте
Я очень много много лет
Мечтаю только о еде
Мне слишком тесно в заперти
И я мечтаю об одном
Скорей свободу обрести
Прогрысть свой ветхий старый дом
Проклятый старый дом
Был дед да помер слепой и жутко злой
Никто не вспомнил о нем зимой холодной
Соседи не стали его тогда хоронить
Лишь доски достали решили заколотить
Двери и окна
Мне больно видеть белый свет
Мне лучше в полной темноте
Я очень много много лет
Мечтаю только о еде
Мне слишком тесно в заперти
И я мечтаю об одном
Скорей свободу обрести
Прогрысть свой ветхий старый дом
Проклятый старый дом
И это место стороной проходит сельский люд
И суеверные твердят-
"Там призраки живут\""""


def count_letters(text):
    result = {}
    text = text.lower()
    for letter in set(text):
        result[letter] = text.count(letter)
    return result


def sort_letters(result):
    out = []
    count = 300
    while count:
        for item in result.items():
            if item[1] == count:
                out.append(item[0])
        count -= 1
    return out


def sort_letters_by_letters(result):
    out = {}
    count = 0
    while count < 1300:
        for item in result.items():
            if ord(item[0]) == count:
                out[item[0]] = item[1]
                break
        count += 1
    return out


def mod_max(arr):
    mod = set()
    count = 0
    for i in set(arr):
        if count < arr.count(i):
            count = arr.count(i)
            mod.clear()
            mod.add(i)
        elif count == arr.count(i) and count != 1:
            mod.add(i)
    return mod


def sum_of_arrs(arr1, arr2):
    return [i + j for i, j in zip(arr1, arr2)]
