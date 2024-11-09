# Matriz aumentada del sistema
A = [
    [0.04, 0.12, 0.15, 16],
    [0.24, 0.10, 0.30, 29],
    [1, 1, 1, 135]
]

# Método de Gauss-Jordan
def gauss_jordan_elimination(matrix):
    rows = len(matrix)

    for i in range(rows):
        # Hacemos que el elemento diagonal sea 1
        diag_factor = matrix[i][i]
        for k in range(len(matrix[i])):
            matrix[i][k] /= diag_factor

        # Hacemos ceros en la columna i en las otras filas
        for j in range(rows):
            if i != j:
                factor = matrix[j][i]
                for k in range(len(matrix[j])):
                    matrix[j][k] -= factor * matrix[i][k]

    # Extraemos las soluciones (última columna)
    solutions = [matrix[i][-1] for i in range(rows)]
    return solutions

# Aplicar el método de Gauss-Jordan
solutions = gauss_jordan_elimination(A)

# Mostrar resultados
print(f"Precio inicial del producto A: ${solutions[0]:.2f}")
print(f"Precio inicial del producto B: ${solutions[1]:.2f}")
print(f"Precio inicial del producto C: ${solutions[2]:.2f}")
