user_str = input('Введите несколько слов: ')

user_str = user_str.split(' ')
i = 1

for element in user_str:
    if len(element) > 10:
        print(f'{i}: {element[:10]}')
    else:
        print(f'{i}: {element}')
    i += 1

print(user_str)