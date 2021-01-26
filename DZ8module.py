import random, copy

def generate_loto_card():
    spectrum = [[1, 9], [10, 19], [20, 29], [30, 39], [40, 49], [50, 59], [60, 69], [70, 79], [80, 90]]
    collon_list = [[], [], [], [], [], [], [], [], []]
    index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    number_comlekt = []
    for i in spectrum:
        current_number_comlekt = [0]
        for j in range(0, 2):
            element = None
            while True:
                ok = 'ok'
                element = random.randrange(i[0], i[1])
                for k in current_number_comlekt:
                    if element == k:
                        ok = ''
                        break
                if ok:
                    current_number_comlekt.append(element)
                    number_comlekt.append(element)
                    break

    randge_list = copy.deepcopy(collon_list)
    for i in number_comlekt:
        start_range = 0
        end_range = 9
        for j in range(0, 9):
            if i >= start_range and i <= end_range:
                randge_list[j].append(i)
            start_range += 10
            end_range += 10
            if end_range == 89:
                end_range = 90
    number_comlekt = randge_list

    index_for_del = []
    index_list_2 = copy.deepcopy(index_list)
    for i in range(0, 3):
        index = random.choice(index_list_2)
        index_list_2.pop(index_list_2.index(index))
        index_for_del.append(index)
    index_for_del = sorted(index_for_del)
    number_comlekt[index_for_del[0]].pop(random.randint(0, 1))
    number_comlekt[index_for_del[1]].pop(random.randint(0, 1))
    number_comlekt[index_for_del[2]].pop(random.randint(0, 1))

    while True:
        multi_sel_index_list = []
        raw_1 = 0
        raw_2 = 0
        raw_3 = 0
        for i in number_comlekt:
            sel_index_list = [[0], [1], [2]]
            index_range = [0, 1, 2]
            for j in i:
                if raw_1 == 5:
                    try:
                        index_range.pop(index_range.index(0))
                    except:
                        pass
                elif raw_2 == 5:
                    try:
                        index_range.pop((index_range.index(1)))
                    except:
                        pass
                elif raw_3 == 5:
                    try:
                        index_range.pop((index_range.index(2)))
                    except:
                        pass
                sel_index = random.choice(index_range)
                if sel_index == 0:
                    raw_1 += 1
                elif sel_index == 1:
                    raw_2 += 1
                elif sel_index == 2:
                    raw_3 += 1
                index_range.pop(index_range.index(sel_index))
                sel_index_list[sel_index].append(j)
            for j in sel_index_list:
                if len(j) == 1:
                    j.append(None)
            multi_sel_index_list.append(sel_index_list)
        element_in_row_1 = 0
        element_in_row_2 = 0
        element_in_row_3 = 0
        for i in multi_sel_index_list:
            if i[0][1]:
                element_in_row_1 += 1
            if i[1][1]:
                element_in_row_2 += 1
            if i[2][1]:
                element_in_row_3 += 1
        if element_in_row_1 == 5 and element_in_row_2 == 5 and element_in_row_3 == 5:
            break

    multi_collomn = []
    for j in range(0, 3):
        collomn = []
        for i in multi_sel_index_list:
            collomn.append(i[j][1])
        multi_collomn.append(collomn)
    return multi_collomn

def loto_card_for_view(loto_card, player):
    name_len = len(str(player))
    v = int((36 - name_len) / 2)
    w = (36 - v - name_len)
    print(f'\n{w * " "}{player}{v * " "}')
    print(36 * '-')
    row = ''
    for i in loto_card:
        for j in i:
            if j:
                if str(j).isdigit():
                    row = row + f' {j:02} '
                else:
                    row = row + f' {j} '
            else:
                row = row + '    '
        row = row + '\n'
    print(row[:-1])
    print(36 * '-')
