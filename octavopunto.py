def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

lista_original = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
lista_invertida_resultante = invertir_lista(lista_original)
print("La lista invertida es:", lista_invertida_resultante)
