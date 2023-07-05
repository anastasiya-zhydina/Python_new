# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Ввод:       Вывод:
# 1 2 3 2 3   2

from random import randint

list_now = [randint(1,10) for i in range(int(input('Введите кол-во эл-ов в массиве: ')))]
print(f'Массив: {list_now}')

def same_number(list: list) -> int:
    count = 0
    for i in range(len(list)-1):
      for j in range(i+1, len(list)):
        if list[i] == list[j]: count += 1
    
    return count

print(f'Число пар в списке: {same_number(list_now)}')