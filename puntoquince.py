import re

def es_palindromo(cadena):
    cadena = re.sub(r'[^\w]', '', cadena.lower())

    return cadena == cadena[::-1]

texto_ingresado = input("Ingresa una cadena de texto: ")

if es_palindromo(texto_ingresado):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
