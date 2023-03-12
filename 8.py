def power(a, n):
    if n == 0:
        return 1
    if n > 0:
        ret = 1
        for i in range(n):
            ret *= a
        return ret
    if n < 0:
        ret = 1
        for i in range(abs(n)):
            ret /= a
        return ret


print(power(2, 0))
print(power(2, 10))
print(power(2, -2))
