import json

with open('DZ_5.7.txt', 'r', encoding='utf-8') as f:
    firm_dict = {}
    file_content = f.readlines()
    gen_profit = 0
    number_of_firm_with_profit = 0
    for i in file_content:
        firm = i.strip().split(' ')
        profit = int(firm[2]) - int(firm[3])
        firm_dict[firm[0]] = profit
        if profit > 0:
            gen_profit += profit
            number_of_firm_with_profit += 1

average_profit = {'average_profit': int(gen_profit/number_of_firm_with_profit)}
finally_list = [firm_dict, average_profit]

print(finally_list)
print(json.dumps(finally_list))

with open('DZ_5.7.json', 'w', encoding='utf-8') as f:
    json.dump(finally_list, f)
