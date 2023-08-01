def calcular_media_aritmetica(lista):
    if len(lista) == 0:
        return None
    suma = sum(lista)
    media = suma / len(lista)
    return media

lista_numeros = [float(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
media_resultante = calcular_media_aritmetica(lista_numeros)

if media_resultante is None:
    print("La lista está vacía, no se puede calcular la media.")
else:
    print("La media aritmética de la lista es:", media_resultante)
