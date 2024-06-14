def get_matrix (n,m,value):
    matrix = []
    for i in range(n):
        str_n = []
        matrix.append(str_n)
        for j in range(m):
            str_n.append(value)
    return matrix
res1 = get_matrix(6,5,4)
print(res1)