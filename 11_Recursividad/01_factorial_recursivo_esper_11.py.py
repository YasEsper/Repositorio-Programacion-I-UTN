# Definimos la función recursiva para calcular el factorial.
def factorial(n):
    # Caso base: si n es 1, devolvemos 1 directamente.
    if n == 1:
        return 1
    else:
        # Paso recursivo: n * factorial de n - 1.
        return n * factorial(n - 1)

# Programa principal.
limite = int(input("¿Hasta qué número querés calcular factoriales?: "))

# Recorremos desde 1 hasta el número ingresado.
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")  # Mostramos el factorial de cada número.
