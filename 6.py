# lesson3

# Задание №6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

i = 1
array = []

num = int(input('Сколько элементов массива Вы хотите ввести? (ввдите целое положительно число):  '))

while i <= num:
    array.append(input('Введите {} число: '.format(i)))
    i += 1

print('Ваш массив выглядит так: ', array)

min_value = array[0]
max_value = array[0]
min_index = 0
max_index = 0
summ_value = 0

for index, value in enumerate(array):
    if int(min_value) > int(value):
        min_value = value
        min_index = index
    if int(max_value) < int(value):
        max_value = value
        max_index = index

if min_index == max_index:
    print('Минимальный и максимальный элемент - одно и то же число')

elif max_index + 1 == min_index or min_index + 1 == max_index:
    print('Между максимальным и минимальным числами нет других чисел')

elif max_index > min_index and max_index + 1 > min_index:
    for i in range(min_index + 1, max_index):
        summ_value += int(array[i])
    print('Сумма элементов между {} и {} = {}'.format(min_value, max_value, summ_value))

elif min_index > max_index and min_index + 1 > max_index:
    for i in range(max_index + 1, min_index):
        summ_value += int(array[i])
    print('Сумма элементов между {} и {} = {}'.format(max_value, min_value, summ_value))
