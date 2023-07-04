# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

'''
def change(n):
    if n==0:
        return ''
    num = int(input())
    return change(n-1)+f' {num}'

n= int(input('Введите число = '))
print(change(n))
'''

def change(n):
    number = input('')
    if n == 1:
        return number
    return change(n-1) + ' ' + number

n = int(input('введите кол-во эл-ов: '))
result = change(n)
print(result)
