# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                 Вывод:
# 7                     3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1        (каждое число вводится с новой строки)

import random

'''
n = int(input('Введите кол-во эл-ов первого массива: '))
ferst = []
for i in range(n): ferst.append(random.randint(1,10))

m = int(input('Введите кол-во эл-ов второго массива: '))
second = []
for i in range(m): second.append(random.randint(1,10))

print(f'Первый массив: {ferst}')
print(f'Второй массив: {second}')

count = 0                         # количество повторений числа во 2 массиве                    
for i in range(n):                # цикл проходится по первому списку
    for j in range(m):            # и по второму, чтобы сравнить числа
        if ferst[i] == second[j]: # сравниваем число из 1 на равенстро с числами 2 списка
            count += 1            # если есть равенство, то счетчик увеличиваем
    if count == 0:                # если счетчик остался равен 0, то выводим на 
        print(ferst[i], end=' ')  # печать элемент 1 массива (в строку)
    count = 0                     # если повторы были, то обнулем счетчик и 
print('\n')                       # переходим к следующему элементу массива
'''

def random_generate_list(len_list):
    list_now = []
    for i in range(len_list): 
        list_now.append(random.randint(1,10))
    return list_now

def difference_list(len_1,len_2):
    list_end = []
    for item in len_1:
        if item not in len_2:
            list_end.append(item)
    return list_end

len_1 = int(input('Введите кол-во эл-ов первого списка: '))
list_1 = random_generate_list(len_1)
len_2 = int(input('Введите кол-во эл-ов второго списка: '))
list_2 = random_generate_list(len_2)

print(f'Первый список: {list_1}')
print(f'Второй список: {list_2}')
list_difference = difference_list(list_1,list_2)
print(f'Эл-ы, которые не повторяются: {list_difference}')