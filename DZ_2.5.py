current_rating = [9, 7, 5, 5, 4, 3]
print(f'Текущее значение рейтинга: {current_rating }')

user_rating = int(input('Введите своё значение рейтинга (целое число): '))

if current_rating[len(current_rating)-1] > user_rating:
    current_rating.insert(len(current_rating), user_rating)
else:
    for i in range(0, len(current_rating)-1):
        if user_rating >= current_rating[i]:
            current_rating.insert(i, user_rating)
            break

print(f'Новое значение рейтинга: {current_rating}')

