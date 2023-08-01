def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5 / 9
    return grados_celsius

grados_fahrenheit_ingresados = float(input("Ingresa la temperatura en grados Fahrenheit: "))
grados_celsius_resultantes = fahrenheit_a_celsius(grados_fahrenheit_ingresados)
print(grados_fahrenheit_ingresados, "grados Fahrenheit son", grados_celsius_resultantes, "grados Celsius.")
