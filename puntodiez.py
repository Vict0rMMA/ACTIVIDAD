def factorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

numero_ingresado = int(input("Ingresa un número entero positivo: "))
factorial_resultante = factorial(numero_ingresado)
print("El factorial de", numero_ingresado, "es:", factorial_resultante)
