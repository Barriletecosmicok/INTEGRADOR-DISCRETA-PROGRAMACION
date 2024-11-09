def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento}\t", end="")
        print()


def gauss_jordan(matriz, soluciones, n):
    for i in range(n):
        pivot = matriz[i][i]
        
        if pivot == 0:
            print(f"Error: pivote cero en fila {i}")
            return
        
        
        for j in range(n + 1):
            matriz[i][j] /= pivot
        
        soluciones[i] = matriz[i][n]
        
        
        for k in range(n):
            if k != i:
                factor = matriz[k][i]
                for j in range(n + 1):
                    matriz[k][j] -= factor * matriz[i][j]
        
        
        if i == 1:
            factor = matriz[2][i]
            for j in range(n + 1):
                matriz[2][j] -= factor * matriz[1][j]


def main():
    n = 3
    
    matriz = [
        [1, 3, 2, 25000],
        [1, 4, 1, 20000],
        [2, 5, 5, 55000]
    ]
    
    soluciones = [0] * n
    
    print("Sistema de ecuaciones:")
    print("x + 3y + 2z = 25,000")
    print("x + 4y + z = 20,000")
    print("2x + 5y + 5z = 55,000")
    print()
    
    print("Matriz aumentada (coeficientes + resultados):")
    mostrar_matriz(matriz)
    print()
    
    gauss_jordan(matriz, soluciones, n)
    
    print("Matriz después de Gauss-Jordan (forma escalonada reducida):")
    mostrar_matriz(matriz)
    
    print("Soluciones después de Gauss-Jordan:")
    for i in range(n):
        print(f"Variable {chr(120 + i)} = {soluciones[i]}")
    print()
    
    print("Dado que z = t, donde t es un parametro libre, y t debe estar en el rango [5000, 8000], las soluciones son:")
    print("x = 40,000 - t")
    print("y = t - 5,000")
    print("z = t")
    print("Donde t esta en el intervalo [5000, 8000].")


if __name__ == "__main__":
    main()
