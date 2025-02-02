list_num = [15, 2, 7, 20, -5, 10, 42]
list2 = [x for x in list_num if x % 2 == 0 or x > 10]
print(list(set(list2)))