user_time = int(input('Введите время в секундах:'))

hours = user_time // 3600
min = (user_time % 3600) // 60
sec = user_time - hours*3600-min*60

print(f'Результат конвертации: {hours}:{min}:{sec}')