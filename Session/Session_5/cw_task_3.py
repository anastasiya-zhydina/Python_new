# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# def List_1(number):
#     if number%2 == 0: return False
#     if number in (1, 2): return True
#     for i in range(3, number):
#         if number%i == 0:
#             return False
#     return True

def check_number(number):
    flag = True
    for i in range(2, number):
        if number%i != 0: continue
        else: flag = False
    return flag

number = int(input('Введите число: '))
print(check_number(number))