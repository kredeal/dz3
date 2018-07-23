# lesson3

# Задание №3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


i = 1
array = []

num = int(input('Сколько элементов массива Вы хотите ввести? (ввдите целое положительно число):  '))

while i <= num:
    array.append(input('Введите {} целое число: '.format(i)))
    i += 1

print('Ваш массив выглядит так: ', array)

min_value = array[0]
max_value = array[0]
min_index = 0
max_index = 0

for index, value in enumerate(array):
    if int(min_value) > int(value):
        min_value = value
        min_index = index
    if int(max_value) < int(value):
        max_value = value
        max_index = index

del array[min_index]
del array[max_index]

array.insert(min_index, max_value)
array.insert(max_index, min_value)

print('Мы поменяли местами максимальный и минимальный элементы, теперь Ваш массив выглядит так: ', array)
