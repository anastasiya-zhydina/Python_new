# Необходимо выбрать два арбуза с минимальной массой и максимальной.
# Пользователь вводит число N - кол-во арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число - 
# это масса соответсвующего арбуза
# нахождение min и max 

'''
n =int(input('Введите кол-во арбузов: '))
max_massa = 0
min_massa = 1000

for i in range(n):
    x = int(input('Введите массу арбуза: '))
    if x > max_massa:
       max_massa = x
    elif x < min_massa:
        min_massa = x
print(min_massa, max_massa)
'''

n = int(input('Введите кол-во арбузов: '))
min_massa = int(input('Введите вес арбуза: '))
max_massa = 0

for _ in range(n-1):
    massa = int(input('Введите вес арбуза: '))
    if massa < min_massa:
        min_massa = massa
    elif massa > max_massa:
        max_massa = massa
print(min_massa, max_massa)