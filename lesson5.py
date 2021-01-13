all_users = ["Gaben", "Tommy", "Turezkiy", "Break", "Zapad"]
arr = [1, 2, 3, 4]

for i, (j, k) in enumerate(zip(all_users, arr)):
    print(i, j, k)


with open("newfile.txt", "w") as file:
    file.write("hellow world")
    for i in range(7):
        file.write(f'{i} \n')


with open("newfile.txt", "r") as file:
    print(file.read())


with open("newfile.txt", "r") as file:
    for row in file:
        print(row)



def read_file_test():
    with open(r"C:\Users\maks1\PycharmProjects\repeat_py\test.txt", 'r') as file:
        result = 0
        for row in file:
            result += float(row)
        print(result)


matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 2, 0, 3],
    [7, 5, 5, 0]
]
print(*matrix, sep="\n")


def sum_matrix(matrix):
    result = 0
    for i in matrix:
        result += sum(i)
    return result


def sum_diagonal_matrix(matrix):
    result = 0
    for i,_ in enumerate(matrix):
        result += matrix[i][i]
    return result


def sum_r_diagonal_matrix(matrix):
    matrix = matrix[::-1]
    result = 0
    for i, _ in enumerate(matrix):
        result += matrix[i][i]
    return result

def sum_diagonal_for_right_matrih(matrix):
    result = 0
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[0]):
            if i == j:
                result += matrix[i][j]
    return result


