def my_func_1(number_1, number_2):
    number_1 ** number_2
    return number_1 ** number_2

def my_func_2(number_1, number_2):
    multi = number_1
    while number_2 + 1 != 0:
        multi = multi * number_1
        number_2 += 1
    return 1/multi

while True:
    number_1 = float(input('Введите положительное число: '))
    if number_1 <= 0:
        print('Неверный ввод')
    else:
        break

while True:
    number_2 = int(input('Введите целое отрицательное число: '))
    if number_2 >= 0:
        print('Неверный ввод')
    else:
        break

print(my_func_1(number_1, number_2))
print(my_func_2(number_1, number_2))
