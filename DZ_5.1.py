with open('DZ_5.1.txt', 'w', encoding='utf-8') as f:
    print('Построчно вводите данные. Для завершения ввода введите пустую строку.')
    while True:
        user_string = input('Введите строку: ')
        if user_string:
            f.write(user_string + '\n')
        else:
            break