from sys import argv

file_name, production, rate, prize = argv

print(f'Заработная плата сотрудника: {float(production) * float(rate) + float(prize)} рублей.')



