my_list = [0, 1, 2, 3, 4, 5, 18, 21, 24, 27, 30]

list1 = [i for i in my_list if i < 5]
print(*list1)

list2 = [i // 2 for i in my_list]
print(*list2)

list3 = [i * 2 for i in my_list if i > 17]
print(*list3)
