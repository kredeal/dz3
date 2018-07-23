# lesson3

# Задание №7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

i = 1
j = 0
array = []

num = int(input('Сколько элементов массива Вы хотите ввести? (ввдите целое положительно число):  '))

while i <= num:
    array.append(input('Введите {} целое число: '.format(i)))
    i += 1
min = array[0]
index_min = 0

print('Ваш массив выглядит так: ', array)
print('\nДва наименьших символа : \n')

while j < 2:

    min = array[0]
    index_min = 0

    for index, value in enumerate(array):
        if int(value) < int(min):
            min = value
            index_min = index

    print(' равен {}\n'.format(min))
    del array[index_min]
    j += 1
