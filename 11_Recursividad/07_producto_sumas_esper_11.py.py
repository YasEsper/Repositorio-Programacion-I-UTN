# Función recursiva para multiplicar usando sumas
def producto(a, b):
    # Caso base: si b es 0, el resultado es 0
    if b == 0:
        return 0
    else:
        # Paso recursivo: sumamos a b veces
        return a + producto(a, b - 1)

# Programa principal
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
resultado = producto(a, b)
print(f"{a} x {b} = {resultado}")
