my_dict = {'One': 'Один', 'Two': 'Два',  'Three': 'Три',  'Four': 'Четыре'}

with open('DZ_5.4.txt', 'r', encoding='utf-8') as f:
    with open('DZ_5.4_2.txt', 'w', encoding='utf-8') as f_2:
        for i in f.readlines():
            f_2.write(my_dict[i.strip().split(' - ')[0]] + ' - ' + i.strip().split(' - ')[1] + '\n')