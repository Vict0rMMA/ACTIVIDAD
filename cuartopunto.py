def es_par(numero):
    return numero % 2 == 0

numero_ingresado = int(input("Ingresa un número: "))

if es_par(numero_ingresado):
    print(numero_ingresado, "es un número par.")
else:
    print(numero_ingresado, "es un número impar.")
