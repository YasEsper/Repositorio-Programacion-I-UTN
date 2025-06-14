# Función recursiva para calcular la potencia
def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    else:
        # Paso recursivo: base * potencia(base, exponente - 1)
        return base * potencia(base, exponente - 1)

# Programa principal
base = int(input("Base: "))
exponente = int(input("Exponente: "))
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")
