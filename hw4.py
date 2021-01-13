def collaci(n):
    from datetime import datetime
    start_time = datetime.now()
    total = {}
    for i in range(2, n):
        count = 0
        i_origin = i
        while i != 1:
            if i % 2:
                i = (i * 3 + 1) / 2
                count += 2
            else:
                i /= 2
                count += 1
            if i in total:
                count += total[i]
                break
        total[i_origin] = count
    count_max = total.values()
    print(max(count_max))
    return print(datetime.now() - start_time)


def collaci_slow(n):
    from datetime import datetime
    start_time = datetime.now()
    total = {}
    for i in range(2, n):
        count = 0
        i_origin = i
        while i != 1:
            if i % 2:
                i = (i * 3 + 1) / 2
                count += 2
            else:
                i /= 2
                count += 1
        total[i_origin] = count
    count_max = total.values()
    print(max(count_max))
    return print(datetime.now() - start_time)


def tr(n):
    if not n % 2:
        print("n chetnoe")
    else:
        print("nechet")


def time_for_me(sl):
    from datetime import datetime
    from time import sleep
    start_time = datetime.now()
    sleep(sl)
    return print(datetime.now() - start_time)
