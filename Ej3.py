# Matriz de coeficientes y vector de términos independientes
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

# Función de eliminación Gauss-Jordan
def gauss_jordan(A, b):
    n = len(A)
    
    # Construir la matriz ampliada
    for i in range(n):
        A[i].append(b[i])

    print("Matriz ampliada inicial:")
    for row in A:
        print(row)
    print()

    # Aplicar eliminación Gauss-Jordan
    for i in range(n):
        # Escalar el pivote a 1
        factor = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= factor

        print(f"\nEscalando fila {i+1} para que el pivote sea 1:")
        for row in A:
            print(row)

        # Hacer ceros en la columna del pivote
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n + 1):
                    A[k][j] -= factor * A[i][j]

                print(f"\nRestando {factor} veces la fila {i+1} de la fila {k+1}:")
                for row in A:
                    print(row)

    # Extraer soluciones
    x = [A[i][n] for i in range(n)]
    return x

# Llamada a la función y mostrar el resultado
x = gauss_jordan(A, b)

print("\nSoluciones:")
for i in range(9):
    print(f"T{i+1} = {x[i]:.2f}")
