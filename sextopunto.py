def calcular_suma_lista(lista):
    suma = sum(lista)
    return suma

lista_numeros = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
suma_resultante = calcular_suma_lista(lista_numeros)
print("La suma de los números en la lista es:", suma_resultante)
