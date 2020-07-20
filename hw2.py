def sum_arr(arr):
    result = 0
    while arr:
        result += arr.pop()
    return result


def sum_arr_1(arr):
    result = 0
    for i in arr:
        result += i
    return result


def sum_arr_2(arr):
    return sum(arr)  # ))))


def average_arr(arr):
    result = 0
    i = 0
    while i < len(arr):
        result += arr[i]
        i += 1
    return result / len(arr)


def geometric_arr(arr):
    result = 1
    for i in arr:
        result *= i
    return result ** (1/len(arr))


def squares_arr(arr):
    result = [i**2 for i in arr]
    return result


def squares_arr_1(arr):
    result = list(map(lambda x: x**2, arr))
    return result


def cumulative_arr(arr):
    result = [sum(arr[:i]) for i in range(1, len(arr))]
    return result


def mediana_arr(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        result = (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
    else:
        result = arr[len(arr) // 2]
    return result


def lower_quartile(arr):
    arr = sorted(arr)
    arr_lower = arr[:len(arr) // 2]
    if len(arr_lower) % 2 == 0:
        result = (arr_lower[len(arr_lower)//2] + arr_lower[len(arr_lower)//2 - 1]) / 2
    else:
        result = arr_lower[len(arr_lower) // 2]
    return result

def upper_quartile(arr):
    arr = sorted(arr)
    arr_upper = arr[(len(arr) // 2) + 1:]
    if len(arr_upper) % 2 == 0:
        result = (arr_upper[len(arr_upper)//2] + arr_upper[len(arr_upper)//2 - 1]) / 2
    else:
        result = arr_upper[len(arr_upper) // 2]
    return result


def upper_quartile_1(arr):
    arr = sorted(arr)
    arr = arr[(len(arr) // 2) + 1:]
    return mediana_arr(arr)


def lower_quartile_1(arr):
    arr = sorted(arr)
    arr = arr[:len(arr) // 2]
    return mediana_arr(arr)


def sort_from_max(arr):
    i = 0
    l = len(arr)
    while i < l:
        i_2 = 0
        while (i_2 + 1) < (l - i):
            if arr[i_2] > arr[i_2 + 1]:
                arr[i_2], arr[i_2 + 1] = arr[i_2 + 1], arr[i_2]
            i_2 += 1
        i += 1
    return arr






