# Función recursiva para repetir una frase
def repetir_frase(n, frase):
    # Caso base: si n es 0, no repetimos más
    if n == 0:
        return
    else:
        print(frase)
        repetir_frase(n - 1, frase)  # Llamamos con n-1

# Programa principal
cantidad = int(input("¿Cuántas veces querés repetir la frase?: "))
frase = input("Ingresá la frase: ")
repetir_frase(cantidad, frase)
