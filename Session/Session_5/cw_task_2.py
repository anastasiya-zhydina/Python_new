# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random

list_lang = int(input('Введите длинну списка оценок Васи: '))
list_1 = []

def create_list():
    for i in range(list_lang):
        list_1.append(random.randint(1,10))
    return list_1

print(f'Изначальные оценки: {create_list()}')

min_mark = min(list_1)
max_mark = max(list_1)

def change(list_1):
    for i in range(len(list_1)):
        if list_1[i] == max_mark:
            list_1[i] = min_mark
    return list_1

print(f'Измененные оценки: {change(list_1)}')