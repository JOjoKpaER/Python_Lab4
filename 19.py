def linear(lst):
    if not lst:
        return lst
    if isinstance(lst[0], list):
        return linear(lst[0]) + linear(lst[1:])
    return lst[:1] + linear(lst[1:])


print(*linear([]))
print(*linear([[1, 2], 4, [[2, 4, 8, [-4, 'er', [0], [{2: 'abc'}, []]]]]]))

