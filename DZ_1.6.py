current_result = int(input('Введите результат первой тренировки (в км):'))
goal = int(input('Введите желаемую цель (в км):'))
improvement = 0.1
i = 1

while goal > current_result:
    print(f'{i}-й день: {round(current_result, 2)} км')
    current_result = current_result*(1 + improvement)
    i += 1
else:
    print(f'{i}-й день: {round(current_result, 2)} км')

print(f'На {i}-й день спортсмен достиг результата не менее {int(current_result)} км')