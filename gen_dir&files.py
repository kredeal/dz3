
import os

def count_task():

    n = 0
    with open("dz.txt") as f:
        for line in f:
            n+=1
    return n

def create_list():
    str = []
    with open('dz.txt') as f:
        for line in f:
            str.append(line)
    return str

def make_dir_with_files(pattern, count, list):

    if not os.path.exists(pattern):
        os.makedirs(pattern)

        os.chdir(pattern)

        for i in range(1, count + 1):

            with open('{}.py'.format(i), 'w', encoding='utf-8') as f:
                f.write('\n#{}\n\n''#Задание №{}\n\n'.format(pattern,list[i-1]))



make_dir_with_files('lesson3', count_task(),create_list())
