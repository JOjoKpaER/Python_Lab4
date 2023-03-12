def partial_sum(*args):
    ret = []
    for i in range(len(args) + 1):
        summ = 0
        for j in range(i):
            summ += args[j]
        ret.append(summ)
    return ret


print(partial_sum(13))
print(partial_sum(1, 0.5, 0.25, 0.125))
