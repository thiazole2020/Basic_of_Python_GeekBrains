def division(number_1, number_2):
    try:
        number_1 / number_2
    except ZeroDivisionError:
        print('Деление на ноль!')
    else:
        return print(f'Результат деления: {float(number_1 / number_2)}')

division(float(input('Введите делимое: ')), float(input('Введите делитель: ')))

