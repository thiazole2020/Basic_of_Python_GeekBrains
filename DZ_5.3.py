with open('DZ_5.3.txt', 'r', encoding='utf-8') as f:
    edge_salary = 20000
    sum_salary = 0
    file_str = f.readlines()

    print(f'Список сотрудников с заработной платой менее {edge_salary}:')
    for i in file_str:
        sum_salary += float(i.split()[1])
        if float(i.split()[1]) < edge_salary:
            print(i.split()[0])

    print(f'Средняя заработная плата по предприятию: {int(sum_salary / len(file_str))}')