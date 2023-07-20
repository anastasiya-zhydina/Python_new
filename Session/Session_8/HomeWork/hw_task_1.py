phones_book = open('phones_book.txt', 'a')
phones_book.close()
# phonesbook = open('phonesbook.txt', 'a')
# phonesbook.close

from pathlib import Path

fail_path = Path('phones_book.txt')
print(fail_path)

# добавление контакта в справочник
def add_contact():
  with open(fail_path, 'a', encoding='utf8') as file:
      file.write('\n')
      file.write(input('Введине ФИО и номер телефона: '))
#add_contact()

# показывает весь справочник
def show_contact():
   with open(fail_path, 'r', encoding='utf8') as file:
      print(file.read())
#show_contact()

# поиск в справочнике
def find_contact():
   list_1 = []
   serch = input('Введите искомы номер или ФИО или их часть: ').strip()
   with open(fail_path, 'r', encoding='utf8') as file:
      for contakt in file:
         if serch in contakt:
            list_1.append(contakt)
      print(*[line for line in list_1])
#find_contact()

def change_contact():
    with open(fail_path, 'r', encoding='utf8') as file:
        phones = file.readlines()
        number = input('Введите номер или ФИО изменяемой строки: ')
        change_line = input('Введите новое ФИО и номер или ничего не вводите для удаления строки: ') + '\n'
        for i in range(len(phones)):
           if phones[i].casefold().find(number) != -1:
              phones[i] = change_contact
        phones = ''.join(phones)
    with open(fail_path, 'w', encoding='utf8') as file:
       file.write(phones)               

def choouse():
    flag = True
    while flag:
        n = input('Выберите действие: \n 1 - добавить контакт, \n 2 - показать контакты, \n 3 - поиск по контактам, \n 4 - внести изменения, \n 5 - завершить работу \n')
        match n:
            case '1':
                add_contact()
            case '2':
                show_contact()
            case '3':
                find_contact()
            case '4':
                change_contact()
            case '5':
                print('Вы завершили работу')
                flag = False
choouse()