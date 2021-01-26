with open('DZ_5.5.txt', 'w', encoding='utf-8') as f:
    f.write(input('Введите набор чисел разделенных пробелом: '))

with open('DZ_5.5.txt', 'r', encoding='utf-8') as f:
    sum = 0
    numbers = f.readlines()
    for i in numbers[0].split(' '):
        sum += int(i)

print(f'Сумма чисел в файле: {sum}')

