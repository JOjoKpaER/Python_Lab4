def recursive_len(lst):
    if len(lst) == 1:
        return 1
    return 1 + recursive_len(lst[0:-1])


print(recursive_len([1, 2, 3]))
