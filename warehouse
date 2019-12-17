# импортирование необходимых модулей:
import datetime
import os
import functions_chest  # файл, содержащий модули специально созданные для данной программы

path = os.getcwd()  # определение путь к папке выполняемого кода


scroll = {}  # создание пустого словаря

# ------приветствие и отображение даты------
input('...press ENTER to begin...')
print('hello!')
print('today is:', datetime.date.today())
if not scroll:
    print('...your database are empty...\n')


# ------обработка ключей и значений------
while True:
    act = (input('what do you want?\n'
                 'add new product - "add"\n'
                 'delete - "delete"\n'
                 'show all products - "show"\n'
                 'for change amount - "change"\n'
                 'quit to program - "end"\n'))
    if act == 'add':
        while True:
            key = (input('enter the new product\n'
                         'or press "go" to continue menu: '))
            if key == '':
                print('sorry, empty area')
                continue
            if key == 'add':
                break
            elif key == 'go':
                break
            elif key in scroll:
                print('sorry, this product already exist...')
                break
            elif key not in scroll:
                value = (input('value: '))
                scroll.setdefault(functions_chest.adding_1(key), functions_chest.adding_2(value))
                print('new product was added!')  # добавление ключа и значения в словарь с помощью setdefault
                continue

# ------удаление элемента из словаря------
    if act == 'delete':
        while True:
            if not scroll:
                print('...your database are empty...')
                break
            print('your products:', scroll.items())
            key_del = str(input('delete item: '))
            if key_del == 'add' or 'show' or 'change' or 'end':
                break
            while True:
                if key_del in scroll.keys():  # проверка наличия ключа в словаре
                    del scroll[key_del]  # перед удалением с помощью метода .keys()
                    break
                else:
                    print('sorry, non existing product.')
                    key_del = str(input('try again: '))
                    if key_del == 'add' or 'show' or 'change' or 'end':
                        break
            print(scroll)

    if act == 'show':
        while 1 == 1:
            if not scroll:
                print('...your database are empty...')
            print('your products:', scroll.items())
            break
# ------изменение значения ключа------
    if act == 'change':
        while True:
            if not scroll:
                print('...your database are empty...')
                break
            print('your products:', scroll.items())
            key_change = input('select product for change value or press "go": ')
            if key_change == 'add' or 'show' or 'delete' or 'end':
                break
            elif key_change not in scroll.keys():
                print('this product not found')
                key_change = input('try again, select product: ')
            elif key_change == '':
                print('sorry, empty area')
                continue
            elif key_change == 'go':
                break
            elif key_change in scroll:
                print('sorry, this product already exist...')
                break
            value_change = input('enter the value to change: ')
            while type(value_change) != int:
                try:
                    value_change = int(value_change)
                except ValueError:
                    print('sorry, value is not suitable')
                    value_change = (input('try again, enter the number: '))
            scroll[key_change] = value_change
    if act == 'end':
        print('...closing the program...')
        print('bye!')
        break
