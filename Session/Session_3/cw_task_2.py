# Дана последовательность из N чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг циклический) на К элементов вправо, К - положительное число.

# list = [1,2,3,4,5,6,7,8,9,0]
# print(list)
# k = int(input('Введите число: '))

# result = list[len(list)-k:len(list)] + list[0:len(list)-k]
# print(result)

a = [1,2,3,4,5,6,7,8,9,0]
k = int(input())
for i in range(k):
    a.insert(0,a.pop())
print(a)