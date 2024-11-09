
A = [
    [4, -1, 0, -1, 0, 0, 0, 0, 0],
    [-1, 4, -1, 0, 0, 0, 0, 0, 0],
    [0, -1, 4, 0, 0, -1, 0, 0, 0],
    [-1, 0, 0, 4, -1, 0, -1, 0, 0],
    [0, -1, 0, -1, 4, -1, 0, -1, 0],
    [0, 0, -1, 0, -1, 4, 0, 0, -1],
    [0, 0, 0, -1, 0, 0, 4, -1, 0],
    [0, 0, 0, 0, -1, 0, -1, 4, -1],
    [0, 0, 0, 0, 0, -1, 0, -1, 4]
]


b = [150, 150, 150, 50, 0, 50, 50, 0, 50]


def gauss_jordan(A, b):
    n = len(A)
    
    
    for i in range(n):
        A[i].append(b[i])

    
    for i in range(n):
        
        factor = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= factor

        
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n + 1):
                    A[k][j] -= factor * A[i][j]

    
    x = [A[i][n] for i in range(n)]
    return x


x = gauss_jordan(A, b)


for i in range(9):
    print(f"T{i+1} = {x[i]:.2f}")
