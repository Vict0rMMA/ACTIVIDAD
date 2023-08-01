import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio_ingresado = float(input("Ingresa el radio del círculo: "))
area_del_circulo = calcular_area_circulo(radio_ingresado)
print("El área del círculo con radio", radio_ingresado, "es:", area_del_circulo)
