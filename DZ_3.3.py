def my_func(number_1, number_2, number_3):
    number_list = [number_1, number_2, number_3]
    number_list.remove(min(number_list))
    return number_list[0]*number_list[1]


print(my_func(float(input('Введите первое число: ')), float(input('Введите второе число: ')), float(input('Введите третье число: '))))

