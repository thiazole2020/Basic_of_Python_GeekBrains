from itertools import count, cycle
#из условия задачи не совсем ясно в каком виде выводить числа. Я реализовал просто вывод на экран

#генератор целых чисел
initial = int(input('Начальное значение: '))
while True:
    end_val = int(input('Конечное значение: '))
    if end_val > initial:
        break
    print('Введите большее значение, чем начальное')

for i in count(initial):
    if i > end_val:
        break
    else:
        print(i)

#повторение элементов списка
my_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
exit_val = 0
for i in cycle(my_list):
    if exit_val > 20:
        break
    print(i)
    exit_val += 1
