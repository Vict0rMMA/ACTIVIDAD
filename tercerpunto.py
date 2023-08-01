import random

def generar_lista_aleatoria(longitud, limite_inferior, limite_superior):
    lista_aleatoria = [random.randint(limite_inferior, limite_superior) for _ in range(longitud)]
    return lista_aleatoria

longitud_lista = int(input("Ingresa la longitud de la lista: "))
limite_inferior = int(input("Ingresa el límite inferior de los números aleatorios: "))
limite_superior = int(input("Ingresa el límite superior de los números aleatorios: "))

lista_aleatoria = generar_lista_aleatoria(longitud_lista, limite_inferior, limite_superior)
print("La lista de números aleatorios es:", lista_aleatoria)
