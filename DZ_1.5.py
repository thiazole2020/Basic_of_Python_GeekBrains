revenue = int(input('Введите значение выручки:'))
cost = int(input('Введите значение издержек:'))
profit = revenue - cost

if profit > 0:
    worker_number = int(input('Введите количество сотрудников:'))
    print('Фирма отработала с прибылью: ', profit)
    print('Рентабельность: ', profit/revenue)
    print('Рентабельность на одного работника: ', profit/worker_number)
elif profit == 0:
    print('Фирма отработала с нулевой прибылью')
else:
    print('Фирма отработала с убытком: ', -profit)
