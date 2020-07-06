
def reverse_digit_1(x):
    x = list(str(x))
    x.reverse()
    x = "".join(x)
    return x

def reverse_digit_2(x):
    result = 0
    while x:
        result = result*10 + x % 10
        x //= 10
    return result

def list_from_digit(x):
    result = []
    while x:
        result.append(x % 10)
        x //= 10
    result.reverse()
    return result

def digit_from_list(x):
    x[::-1]
    result = ""
    while x:
        result += str(x.pop())
    return int(result)





