my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

end_list = [my_list[i] for i in range(len(my_list)) if len([j for j,x in enumerate(my_list) if x == my_list[i]]) == 1]

print(end_list)