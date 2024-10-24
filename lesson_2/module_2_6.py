def get_matrix(n:int, m:int, value):
    res_matrix = []
    for k in range(0, n):
        row = []
        for j in range(0, m):
            row.append(value)
        res_matrix.append(row)
    return res_matrix

matrix = get_matrix(5,3,'x')
for i in range(0, len(matrix)):
    print(matrix[i])