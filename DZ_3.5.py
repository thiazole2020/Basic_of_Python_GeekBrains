def sum_of_numbers():
    numbers = []
    exit_symbol = False
    while True:
        print('Для выхода введите "Q"')
        current_numbers = input('Введите числа, разделененные пробелом: ')
        current_numbers = current_numbers.split()

        for i in range(len(current_numbers)):
            if current_numbers[i].upper() == 'Q':
                exit_symbol = True
                continue
            current_numbers[i] = float(current_numbers[i])
            numbers.append(current_numbers[i])

        sum_of_numbers = sum(numbers)
        print(f'Сумма введенных вами чисел: {sum_of_numbers}')

        if exit_symbol == True:
            break
    print('Работа программы завершена.')


sum_of_numbers()



