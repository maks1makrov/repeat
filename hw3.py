def simple_digits(digit):
    result = []
    for div in range(1, digit+1):
        for i in range(2, div):
            if div % i == 0:
                break
        else:
            result.append(div)
    return result


def perfekt_digits(digit):
    reselt = []
    for div in range(1, digit+1):
        total = 0
        for i in range(1, div):
            if not div % i:
                total += i
        if total == div:
            reselt.append(div)
    return reselt


def armstrongs_digits(digit):
    result = []
    for i in range(1, digit):
        i = str(i)
        lenth = len(i)
        total = 0
        for div in i:
            total += int(div) ** lenth
        if total == int(i):
            result.append(i)
    return result


def semi_perfekt_digits(digit):
    reselt = []
    for div in range(1, digit+1):
        total = 0
        for i in range(1, div):
            if not div % i:
                total += i
                if total >= div:
                    reselt.append(div)
                    break
    return reselt


def semi_perfekt_digits_1(digit):
    from itertools import combinations
    result = []
    for div in range(1, digit+1):
        total = []
        for i in range(1, div):
            if not div % i:
                total.append(i)
        for i in range(1, len(total) + 1):
            if div in list(map(sum, combinations(total, i))):
                result.append(div)
                break
    return result


