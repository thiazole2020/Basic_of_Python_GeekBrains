def user_data(name, surname, year, city, phone, email):
    return print(f'Данные пользователя: {name} {surname}, год рождения: {year}, город проживания: {city}, телефон: {phone}, E-mail: {email}')

user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_year = input('Введите год рождения: ')
user_city = input('Введите город проживания: ')
user_phone = input('Введите телефон: ')
user_email = input('Введите E-mail: ')

user_data(name=user_name, surname=user_surname, year=user_year, city=user_city, phone=user_phone, email=user_email)
