list = []

print('Ввод пустого значения означает выход из цикла')
while True:
    element = input('Введите элемент списка: ')
    if element != '':
        list.append(element)
    else:
        break

print('Введеный список: ', list)

#выделение последнего нечетного элемента и удаление его из списка, но с сохраненим его в отдельную переменную
last_odd_element = []

if len(list) % 2 != 0:
    last_odd_element = list.pop()

#перемешивание элементов

list_length = range(0, len(list), 2)
for i in range(0, len(list), 2):
    current_element = list[i]
    del list[i]
    list.insert(i + 1, current_element)

#добавление нечетного символа, который был выделен ранее
if last_odd_element != []:
    list.append(last_odd_element)

print('Список после перемешивания элементов: ', list)