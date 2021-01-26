with open('DZ_5.6.txt', 'r', encoding='utf-8') as f:
    my_dict = {}
    for i in f.readlines():
        discipline = i.strip().split(' ')
        hours = 0
        for j in discipline[1:]:
            if j.find('(') > 0:
                hours += int(j[:j.find('(')])
        my_dict[discipline[0][:-1]] = hours

print(my_dict)