# Función recursiva para calcular la serie de Fibonacci.
def fibonacci(n):
    # Caso base 1: el primer término es 0.
    if n == 0:
        return 0
    # Caso base 2: el segundo término es 1.
    elif n == 1:
        return 1
    else:
        # Paso recursivo: suma de los dos términos anteriores.
        return fibonacci(n - 1) + fibonacci(n - 2)

# Programa principal.
terminos = int(input("¿Cuántos términos de Fibonacci querés ver?: "))

# Imprimimos desde f(0) hasta f(n-1).
for i in range(terminos):
    print(f"f({i}) = {fibonacci(i)}")  # Mostramos cada término de la serie.
