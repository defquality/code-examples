def adding_1(a):  # создание функции для обработки ключа
    while a == '':
        print('empty area')
        a = str(input('try again to enter key: '))
        if a == '':
            print('empty area')
            a = str(input('try again to enter key: '))
    return a


def adding_2(b):  # создание функции для обработки значения
    while type(b) != int:
        try:
            b = int(b)
        except ValueError:
            print('sorry, value is not suitable')
            b = (input('try again, enter the number: '))
    return b
