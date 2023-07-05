# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arifmetic_prigression(start_number, step_number, quantity_number):
    list_now = [start_number]
    for i in range(1,quantity_number): list_now.append(list_now[i-1] +step_number)
    return list_now

a = int(input('Введите число - начало массива: '))
b = int(input('Введите число - шаг: '))
c = int(input('Введите число - количество эл-ов: '))

arrey_1 = arifmetic_prigression(a,b,c)
print(f'Массив, заполненный эл-ми арифметической прогрессии: {arrey_1}')
        