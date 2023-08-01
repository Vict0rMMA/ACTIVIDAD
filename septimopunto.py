def encontrar_max_y_min(lista):
    numero_mas_grande = max(lista)
    numero_mas_pequeno = min(lista)
    return numero_mas_grande, numero_mas_pequeno

lista_numeros = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
maximo, minimo = encontrar_max_y_min(lista_numeros)
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)
