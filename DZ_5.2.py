with open('DZ_5.2.txt', 'r', encoding='utf-8') as f:
    file_str = f.readlines()
    print(f'Количество строк в файле: {len(file_str)}')
    for i in file_str:
       print(f'Количество слов в строке {file_str.index(i) + 1}: {len(i.split(" "))}')
