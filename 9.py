# lesson3

# Задание №9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

size1 = 3
size2 = 4

i = 0
j = 0
matrix = []
matrix_temp = []
min_num = 0 * size1

print('\nЗаполните матрицу {}x{}\n'.format(size1, size2))

for i in range(size2):

    for j in range(size1):
        matrix_temp.append(int(input('Введите число: ')))

    min_num = matrix_temp
    matrix.append(matrix_temp)
    matrix_temp = []

print()

for line in matrix:

    for i, item in enumerate(line):
        print('{:>6}'.format(item), end='')
        if min_num[i] > item:
            min_num[i] = item

    print()

print('\nМаксимальный элемент среди минимальных элементов столбцов матрицы = ', max(min_num))
