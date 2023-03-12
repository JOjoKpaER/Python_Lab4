def triangle(a, b, c):
    if a >= b + c:
        print("Это не треугольник")
        return
    if b >= a + c:
        print("Это не треугольник")
        return
    if c >= a + b:
        print("Это не треугольник")
        return
    print("Это треугольник")
    return


triangle(1, 1, 2)
triangle(7, 6, 10)
triangle(20, 13, 17)
