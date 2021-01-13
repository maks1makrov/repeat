def reverse_digit_1(x):
    x = list(str(x))
    x.reverse()
    x = "".join(x)
    return x


def reverse_digit_2(x):
    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10
    return result


def list_from_digit(x):
    result = []
    while x:
        result.append(x % 10)
        x //= 10
    result.reverse()
    return result


def digit_from_list(arr):
    arr[::-1]
    result = ""
    while arr:
        result += str(arr.pop())
    return int(result)


def digit_from_list_1(arr):
    result = ""
    while arr:
        result += str(arr.pop(0))
    return int(result)


def digit_from_list_2(arr):
    result = ""
    i = 0
    while i < len(arr):
        result += str(arr[i])
        i += 1
    return int(result)
