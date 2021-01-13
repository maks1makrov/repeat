def discont():
    discont_1 = 1
    discont_2 = 3
    discont_3 = 5
    price_dis_1 = 20
    price_dis_2 = 50
    price_dis_3 = 100
    price = float(input("enter price "))
    if price >= price_dis_3:
        discont_price = format(discont_3 * price / 100, '.2f')
        print(f"your discont is {discont_3}% - {discont_price} rub")
    elif price >= price_dis_2:
        discont_price = format(discont_2 * price / 100, '.2f')
        print(f"your discont is {discont_2}% - {discont_price} rub")
    elif price >= price_dis_1:
        discont_price = format(discont_1 * price / 100, '.2f')
        print(f"your discont is {discont_1}% - {discont_price} rub")
    total = price - float(discont_price)
    print(f"total price is {total}")


def foo_bar():  # bar - 3, foo - 5, foobar - 3 and 5
    first_div = 3
    second_div = 5
    for_3 = "bar"
    for_5 = "foo"
    for_3_and_5 = "foobar"
    for digit in range(1, 100):
        if digit % first_div == 0 and digit % second_div == 0:
            print(digit, for_3_and_5)
        elif digit % first_div == 0:
            print(digit, for_3)
        elif digit % second_div == 0:
            print(digit, for_5)
    return "done"


def sum_of_digit():  # в диапазоне всех lenth_digit значных чисел выводит count чисел, сумма цифр которых равна digit
    digit = int(input("enter digit"))
    lenth_digits = 5
    count = 5
    result = []
    for i in range(10 ** (lenth_digits - 1), 10 ** lenth_digits):
        list_digit = list(map(int, list(str(i))))
        if sum(list_digit) == digit:
            result.append(i)
            count -= 1
            if count == 0:
                break
    return result


def polindrom():
    while True:
        row = input("enter word, for exit enter '0'")
        if row == '0':
            break
        elif row == row[::-1]:
            print(f"{row} is polindrom")
        else:
            print(f"{row} is NOT polindrom")
    pass


def digits_polindroms(first=10, second=10000):
    result = []
    for i in range(first, second):
        i = str(i)
        if i == i[::-1]:
            result.append(int(i))
    return result

def digits_polindroms_1(first=10, second=100):
    result = [i for i in range(first, second) if str(i) == str(i)[::-1]]
    return result
