inital_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
end_list = []
#из условия задания не ясно что делать с первым элементом. Его оставлять всегда или всегда выбрасывать, а может быть сравнивать с последним?

end_list = [inital_list[i] for i in range(1, len(inital_list)) if inital_list[i] > inital_list[i - 1]]
print(end_list)