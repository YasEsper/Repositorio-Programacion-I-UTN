# Función recursiva para sumar los primeros n números
def suma_numeros(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    else:
        # Paso recursivo: sumamos n más la suma anterior
        return n + suma_numeros(n - 1)

# Programa principal
n = int(input("¿Hasta qué número querés sumar?: "))
resultado = suma_numeros(n)
print(f"La suma de los primeros {n} números es: {resultado}")
