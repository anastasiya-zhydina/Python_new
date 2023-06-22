# Напишите программу, которая на вход принимает строку и отслеживает, 
# сколько раз каждый символ уже встречался. Кол-во повторов добаавляется к символам
# с помощью префикса _n

#input = 'a s d f r e w q a s d f c x z'
#string = input.split()
string = input('Введите элементы списка через пробел: ').split()
list = {}
for i in range(len(string)):
    if string[i] not in list.keys():
        list[string[i]] = 1
        print(f'{string[i]} ', end= '')
    else:
        print(f'{string[i]}_{list[string[i]]} ', end= '')
        list[string[i]] += 1
