#Definimos funciones para operaciones que recibe dos parametro a y b.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)  # Devolvemos todos los resultados de la op. una tupla.

# Programa principal
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

# Desempaquetamos la tupla
suma, resta, multi, div = operaciones_basicas(a, b)

print(f"Suma: {suma}") # Mostramos en pantalla la suma. 
print(f"Resta: {resta}") # Mostramosen pantalla la resta.
print(f"Multiplicación: {multi}") # Mostramos en pantalla la multiplicacion.
print(f"División: {div:.2f}")  # Mostramos en pantalla la divisio, con dos decimales {div:.2f}.