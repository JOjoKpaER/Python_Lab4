def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))]
              for i in range(len(matrix[0]))]


matrix1 = [[1]]
matrix1 = transpose(matrix1)
for li in matrix1:
    print(*li)

matrix2 = [[1, 2],
           [3, 4]]
matrix2 = transpose(matrix2)
for li in matrix2:
    print(*li)
