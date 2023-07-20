# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. 
# Ваша программа не должна быть линейной

# 1. Ф-я вывода контактов.
# 2. Ф-я поиска контакта.
# 3. Ф-я добавления контакта.

phones_book = open('phones_book.txt', 'a')

from pathlib import Path

fail_path = Path('phones_book.txt')
print(fail_path)

def add_contact():
  with open(fail_path, 'a', encoding='utf8') as file:
      info=input('Введите данные: ')
      file.writelines(f'\n{info}')

#add_contact()

def show_contact():
   with open(fail_path, 'r', encoding='utf8') as file:
      #print([lines for lines in file], set='\n') # set='\n' -> выводит данные в файле .txt в столбик через пробел
      #print(file.readlines())
      print(*[line for line in file]) # * -> выводит данные в файле .txt в столбик

#show_contact()

def find_contact():
   list_1 = []
   serch = input('Поиск: ').strip()
   with open(fail_path, 'r', encoding='utf8') as file:
      for contakt in file:
         if serch in contakt:
            list_1.append(contakt)
      print(*[line for line in list_1])

#find_contact()

def choouse():
    flag = True
    while flag:
        n = input('Выберите действие (1 - добавить контакт, 2 - показать контакты, 3 - поиск по контактам, 4 - завершить работу): ')
        match n:
            case '1':
                add_contact()
                #flag = False
            case '2':
                show_contact()
                #flag = False
            case '3':
                find_contact()
                #flag =False
            case '4':
                print('Вы завершили работу')
                flag = False

choouse()
