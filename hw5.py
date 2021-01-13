def Zaliz():
    result = {}
    with open(r'C:\Users\maks1\Documents\new\lesson5\f.txt', 'r') as file:
        for row in file:
            row_origin = row
            row = sorted(list(row.strip()))
#            print(row, row_origin)
            if row in result:
                result[row].add(row_origin)
            else:
                result[row] = {row_origin}
    with open(r'C:\Users\maks1\Documents\new\lesson5\result_for_hw5', 'w') as file:
        for value in result.values():
            file.write(value)
    pass

