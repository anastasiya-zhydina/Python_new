# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def index_element(list, min,max):
    list_1 = []
    for i in range(len(list)):
        if max >= list[i] >= min: list_1.append(i)
    return list_1

list_now = [randint(1,10) for i in range(int(input('Введите кол-во эл-ов в массиве: ')))]
print(f'Массив: {list_now}')

b_min = int(input('Введите число - минимум: '))
a_max = int(input('Введите число - максимум: '))

massiv = index_element(list_now, b_min, a_max)
print(f'Индексы элементов, принадлежвщих заданному диапазону в массиве: {massiv}')
