# lesson3

# Задание №4. Определить, какое число в массиве встречается чаще всего.


i = 1
max_count = 0
max_count_value = 0
array = []

num = int(input('Сколько элементов массива Вы хотите ввести? (ввдите целое положительно число):  '))

while i <= num:
    array.append(input('Введите {} число: '.format(i)))
    i += 1

print('Ваш массив выглядит так: ', array)

for index, value in enumerate(array):

    spam = value
    eggs = 0

    for i in array:
        if i == spam:
            eggs += 1

    if max_count < eggs:
        max_count = eggs
        max_count_value = value

if max_count == 1:
    print('Всех чисел поравну')
else:
    print('Число {} встречается в вашем массиве максимальное количетсво раз - {} раз(а)'.format(max_count_value,
                                                                                                max_count))
