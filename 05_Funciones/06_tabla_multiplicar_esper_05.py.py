#Definimos funcion para realizar la tabla de multiplicar del 1 al 10.
def tabla_multiplicar(numero):
    for i in range(1, 11):  # Recorremos del 1 al 10
        print(f"{numero} x {i} = {numero * i}")  # Mostramos cada multiplicación

# Programa principal
num = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)  # Llamamos a la función 
