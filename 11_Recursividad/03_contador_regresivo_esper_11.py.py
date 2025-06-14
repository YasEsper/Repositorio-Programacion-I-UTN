# Función recursiva para contar hacia atrás
def contar_regresivo(n):
    # Caso base: cuando n es 0, detenemos la recursión
    if n == 0:
        return
    else:
        print(n)  # Mostramos el número actual
        contar_regresivo(n - 1)  # Llamamos a la función con n-1

# Programa principal
numero = int(input("Contar hacia atrás desde: "))
contar_regresivo(numero)
