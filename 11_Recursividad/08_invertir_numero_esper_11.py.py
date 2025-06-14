# Función recursiva para invertir un número
def invertir_numero(n):
    # Caso base: si el número tiene un solo dígito
    if n < 10:
        return str(n)
    else:
        # Paso recursivo: último dígito + invertir el resto
        return str(n % 10) + invertir_numero(n // 10)

# Programa principal
numero = int(input("Ingresá un número para invertir: "))
invertido = invertir_numero(numero)
print(f"Número invertido: {invertido}")
