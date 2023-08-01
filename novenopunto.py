def generar_matriz(filas, columnas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

filas = int(input("Ingresa el número de filas de la matriz: "))
columnas = int(input("Ingresa el número de columnas de la matriz: "))

matriz_generada = generar_matriz(filas, columnas)

print("La matriz generada es:")
imprimir_matriz(matriz_generada)
