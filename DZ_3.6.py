def int_func(text):
    return text.capitalize()

def int_func_2(text_2):
    text_2 = text_2.split()
    for i in range(len(text_2)):
        text_2[i] = int_func(text_2[i])
    text_2 = ' '.join(text_2)
    return text_2


print(int_func(input('Введите слово: ')))
print(int_func_2(input('Введите набор слов: ')))