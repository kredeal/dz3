# lesson3

# Задание №8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

size = 4

i = 0
j = 0
matrix = []
matrix_temp = []

print('Заполните матрицу 4х4\n')

for i in range(size):

    for j in range(size):
        matrix_temp.append(input('Введите число: '))

    matrix.append(matrix_temp)
    matrix_temp = []

print()

for line in matrix:
    summ_str = 0

    for i, item in enumerate(line):
        summ_str += int(item)
        print('{:>6}'.format(item), end='')

    print('{:>6}'.format(summ_str))
    print()
