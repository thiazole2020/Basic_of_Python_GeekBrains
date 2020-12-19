number = -1

while number < 0:
    number = int(input('Введите целое положительное число:'))

max_number = number % 10    #выделение последнего числа - остатка от деления на 10
number = number // 10
while number > 0:
    if number % 10 > max_number:
        max_number = number % 10
    number = number // 10

print(max_number)
