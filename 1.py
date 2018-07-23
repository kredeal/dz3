# lesson3

# Задание №1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.


import random

first_list = [x for x in range(2, 100)]
secont_list = [x for x in range(2, 10)]

for i in secont_list:
    print('\nЧисла кратные {} : '.format(i),end='')
    for j in first_list:
        if j % i == 0:
            print(j,end=', ')

