goods = []
i = 1

while True:
    current_name = input('Введите наименование товара: ')
    if current_name == '':
        break
    current_cost = float(input('Введите цену единицы товара: '))
    current_number = float(input('Введите количество товара: '))
    current_unit = input('Введите еденицу хранения: ')
    goods_i = (i, {
        'name': current_name,
        'cost': current_cost,
        'number': current_number,
        'unit': current_unit
        })
    goods.append(goods_i)
    i = i + 1

print(f'Товары: {goods}')

analytics = {'name':'', 'cost':'', 'number':'', 'unit':''}
goods_name = []
goods_cost = []
goods_number = []
goods_unit = []

for j in goods:
    current_name = j[1]['name']			#выделение наименование товара из словаря для текущего товара
    current_cost = j[1]['cost']
    current_number = j[1]['number']
    current_unit = j[1]['unit']
    goods_name.append(current_name)
    goods_cost.append(current_cost)
    goods_number.append(current_number)
    goods_unit.append(current_unit)

analytics['name'] = goods_name
analytics['cost'] = goods_cost
analytics['number'] = goods_number
analytics['unit'] = goods_unit

print(f'Аналитика по товарам: {analytics}')







