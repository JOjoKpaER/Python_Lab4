def matrix(*args):
    try:
        return [[args[2] for i in range(args[0])]
                for j in range(args[1])]
    except:
        try:
            return [["0" for i in range(args[0])]
                    for j in range(args[1])]
        except:
            try:
                return [["0" for i in range(args[0])]
                        for j in range(args[0])]
            except:
                return ["0"]


mtrx1 = matrix()
for li in mtrx1:
    print(*li)

mtrx2 = matrix(2, 3, "a")
for li in mtrx2:
    print(*li)
