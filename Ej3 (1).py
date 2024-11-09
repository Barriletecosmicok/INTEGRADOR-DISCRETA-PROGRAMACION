# Matriz de coeficientes A
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

# Vector de términos independientes b
b = [150, 150, 150, 50, 0, 50, 50, 0, 50]

# Función para realizar el método de Gauss-Jordan
def gauss_jordan(A, b):
    n = len(A)
    
    # Crear matriz aumentada
    for i in range(n):
        A[i].append(b[i])

    # Aplicar eliminación Gaussiana
    for i in range(n):
        # Hacer que el elemento de la diagonal sea 1
        factor = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= factor

        # Hacer ceros en la columna i para todas las filas excepto la fila i
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n + 1):
                    A[k][j] -= factor * A[i][j]

    # Extraer la solución
    x = [A[i][n] for i in range(n)]
    return x

# Resolver el sistema
x = gauss_jordan(A, b)

# Imprimir la solución
for i in range(9):
    print(f"T{i+1} = {x[i]:.2f}")
